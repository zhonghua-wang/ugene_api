# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from job import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Report)
class ReportAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ReportUnit)
class ReportUnitAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Mutant)
class MutantAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    pass
