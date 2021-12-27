from django.shortcuts import render, redirect
from .forms import DataWeeksForm
from week.models import DataWeeks

from datetime import datetime
from isoweek import Week

dict_month = {
    'Январь': 1, 'Февраль': 2, 'Март': 3,
    'Апрель': 4, 'Май': 5, 'Июнь': 6,
    'Июль': 7, 'Август': 8, 'Сентябрь': 9,
    'Октябрь': 10, 'Ноябрь': 11, 'Декабрь': 12
}


def index(requests):
    dates = DataWeeks.objects.all()
    dates_data = {}
    for date in dates:
        date_name = date.day + str(date.month) + date.year
    context = {'dates': dates}
    return render(requests, 'week/index.html', context=context)


def data_weeks_create(request):
    if request.method == 'POST':
        form = DataWeeksForm(request.POST)
        if form.is_valid():
            day = form.cleaned_data['day']
            month = str(form.cleaned_data['month'])
            year = form.cleaned_data['year']

            if len(day) == 2 and len(year) == 4 and day.isdigit() and year.isdigit() and int(year) >= 2019:
                try:
                    datetime(year=int(year), month=dict_month[month], day=int(day))
                    DataWeeks.objects.create(**form.cleaned_data)
                    calculated_weeks(int(day), dict_month[month], int(year))
                    return redirect('index')
                except:
                    form = DataWeeksForm()
            else:
                form = DataWeeksForm()
    else:
        form = DataWeeksForm()
    return render(request, 'week/create_date.html', {'form': form})


def calculated_weeks(day, month, year):
    '''Рассчитывает номер недели'''
    main_date = datetime(2019, 1, 1)
    calculated_date = datetime(year, month, day)

    count = 0
    difference = calculated_date.year - main_date.year

    if difference == 0:
        c = date_week(calculated_date)
        count = Week.__str__(c)[-2:]
    else:
        for c in range(1, difference + 1):
            if main_date.year + c != calculated_date.year:
                c = count_week(main_date.year + c)
                count += c
            else:
                tmg = ''
                c = date_week(calculated_date)
                tmp = Week.__str__(c)
                count += int(tmp[-2:])

    date = list(DataWeeks.objects.all())
    date_w = date[-1]
    date_w.number_week = count
    date_w.save()


def count_week(year):
    return Week.last_week_of_year(year).week


def date_week(date):
    return Week.withdate(date)

