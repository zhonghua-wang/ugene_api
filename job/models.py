# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from hashid_field import HashidAutoField
from ugene_api import settings


class User(AbstractUser):
    id = HashidAutoField(primary_key=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)

    def get_full_name_cn(self):
        return self.last_name + self.first_name

    def __unicode__(self):
        return self.get_full_name_cn() or str(self.username)


class Report(models.Model):
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=1024)
    conclusion = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(_('date created'), default=timezone.now)


class ReportUnit(models.Model):
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=1024)
    report = models.ForeignKey(Report)
    image = models.ImageField(upload_to=settings.UPLOAD_FOLDER, max_length=256, null=True, blank=True)
    data = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(_('date created'), default=timezone.now)


class Job(models.Model):
    id = HashidAutoField(primary_key=True)
    user = models.ForeignKey(User)
    gene_name = models.CharField(max_length=64, blank=True, null=True)
    gene_sequence = models.TextField(null=True, blank=True)
    report = models.ForeignKey(Report, null=True, blank=True)
    created_at = models.DateTimeField(_('date created'), default=timezone.now)


class Mutant(models.Model):
    id = HashidAutoField(primary_key=True)
    job = models.ForeignKey(Job)
    position = models.IntegerField()
    original = models.CharField(max_length=4)
    mutation = models.CharField(max_length=4)
