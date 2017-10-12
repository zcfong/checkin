from django.contrib import admin
from app.models import ContactSeat, Active
from import_export import resources, fields
from django import forms

from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from django_select2.forms import (ModelSelect2Widget)


class ContactSeatResource(resources.ModelResource):
    active = fields.Field(
        column_name='active',
        attribute='active',
        widget=ForeignKeyWidget(Active, 'title'))

    class Meta:
        model = ContactSeat
        fields = ('id', 'active', 'guest', 'seat',)


class ActiveWidget(ModelSelect2Widget):
    search_fields = ('name__icontains',)


class ActiveForm(forms.ModelForm):
    class Meta:
        model = Active
        fields = '__all__'
        widgets = {
            'active': ActiveWidget(queryset=Active.objects.all())
        }


@admin.register(ContactSeat)
class ContactSeatAdmin(ImportExportModelAdmin):
    resource_class = ContactSeatResource
    list_display = ('active', 'guest', 'seat', 'is_sign',)
    search_fields = ('guest', 'seat',)
    list_filter = ('is_sign', 'active__title',)
    ordering = ('-createtime',)
    form = ActiveForm


@admin.register(Active)
class ActiveAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
