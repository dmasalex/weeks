from django.db import models


class Month(models.Model):
    '''Месяц'''
    month = models.CharField('Месяц', max_length=10, blank=False)

    def __str__(self):
        return '{}'.format(self.month)

    class Meta:
        verbose_name = 'Месяц'
        verbose_name_plural = 'Месяца'


class DataWeeks(models.Model):
    '''Данные недели'''
    day = models.CharField('День месяца', max_length=2, blank=False)
    month = models.ForeignKey(Month, related_name='dataweeks', on_delete=models.CASCADE)
    year = models.CharField('Год', max_length=4, blank=False)
    create_date = models.DateField('Дата создания', auto_now=True)
    number_week = models.CharField('Номер недели', max_length=10, blank=True, null=True)

    def __str__(self):
        return '{}.{}.{}'.format(self.day, self.month, self.year)

    def display_month(self):
        return self.month

    class Meta:
        verbose_name = 'Дата'
        verbose_name_plural = 'Даты'