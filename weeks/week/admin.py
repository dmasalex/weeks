from django.contrib import admin

from week.models import Month, DataWeeks


class MonthAdmin(admin.ModelAdmin):
    list_display = ('month', )

class DataWeeksAdmin(admin.ModelAdmin):
    list_display = ('day', 'month', 'year', 'number_week', 'create_date')


admin.site.register(Month, MonthAdmin)
admin.site.register(DataWeeks, DataWeeksAdmin)
