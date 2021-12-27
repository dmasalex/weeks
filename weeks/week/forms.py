from django import forms
from .models import Month


class DataWeeksForm(forms.Form):
    day = forms.CharField(label='Укажи день (двухзначное число, от 01 до 31):')
    month = forms.ModelChoiceField(label='Выбери месяц',empty_label='Месяц...', queryset=Month.objects.all())
    year = forms.CharField(label='Укажи год (четырехзначное число, начиная с 2019г.):')
