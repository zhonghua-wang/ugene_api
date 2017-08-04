# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from job import models


class ReportUnitInline(admin.StackedInline):
    model = models.ReportUnit


class ReportInline(admin.TabularInline):
    model = models.Report
    max_num = 1


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Report)
class ReportAdmin(admin.ModelAdmin):
    inlines = [
        ReportUnitInline,
    ]


@admin.register(models.ReportUnit)
class ReportUnitAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Mutant)
class MutantAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    inlines = [
        ReportInline,
    ]
