from django.contrib import admin
from .models import Hospital


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    empty_value_display = '-empty-'

