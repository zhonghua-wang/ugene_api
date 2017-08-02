from rest_framework import serializers
from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField
#from hashid_field.rest import HashidSerializerCharField
from job import models


class UserSerializer(DynamicModelSerializer):
    class Meta:
        model = models.User
        exclude = []


class ReportSerializer(DynamicModelSerializer):
    class Meta:
        model = models.Report
        exclude = []


class ReportUnitSerializer(DynamicModelSerializer):

    class Meta:
        model = models.ReportUnit
        exclude = []


class JobSerializer(DynamicModelSerializer):
    class Meta:
        model = models.Job
        exclude = []


class MutantSerializer(DynamicModelSerializer):
    class Meta:
        model = models.Mutant
        exclude = []
