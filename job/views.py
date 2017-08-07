# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics, permissions
from dynamic_rest.viewsets import DynamicModelViewSet
from hashid_field import descriptor
from . import models, serializers


class UserViewSet(DynamicModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    permission_classes = (permissions.IsAuthenticated,)
    ordering = ('username',)

    # def get_queryset(self, *args, **kwargs):
    #     user = self.request.user
    #     is_admin = user.is_superuser
    #     if is_admin:
    #         return models.User.objects.all()
    #     else:
    #         return models.User.objects.filter(id=user.id)

class ReportViewSet(DynamicModelViewSet):
    queryset = models.Report.objects.all()
    serializer_class = serializers.ReportSerializer

    permission_classes = (permissions.IsAuthenticated,)

    ordering = ('name',)


class ReportUnitViewSet(DynamicModelViewSet):
    queryset = models.ReportUnit.objects.all()
    serializer_class = serializers.ReportUnitSerializer

    ordering = ('report', 'name')


class JobViewSet(DynamicModelViewSet):
    queryset = models.Job.objects.all()
    serializer_class = serializers.JobSerializer
    permission_classes = (permissions.IsAuthenticated, )

    ordering = ('-created_at', )


class MutantViewSet(DynamicModelViewSet):
    queryset = models.Mutant.objects.all()
    serializer_class = serializers.MutantSerializer

    ordering = ('job', 'position')
