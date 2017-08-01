from rest_framework import serializers
from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField
from hashid_field.rest import HashidSerializerCharField
from job import models


class UserSerializer(DynamicModelSerializer):
    id = HashidSerializerCharField(source_field='job.User.id')

    class Meta:
        model = models.User
        exclude = []


class ReportSerializer(DynamicModelSerializer):
    id = HashidSerializerCharField(source_field='job.Report.id')

    class Meta:
        model = models.Report
        exclude = []


class ReportUnitSerializer(DynamicModelSerializer):
    id = HashidSerializerCharField(source_field='job.ReportUnit.id')
    report = serializers.PrimaryKeyRelatedField(
        pk_field=HashidSerializerCharField(source_field='job.Report.id'),
        read_only=True
    )

    class Meta:
        model = models.ReportUnit
        exclude = []


class JobSerializer(DynamicModelSerializer):
    id = HashidSerializerCharField(source_field='job.Job.id')
    user = serializers.PrimaryKeyRelatedField(
        pk_field=HashidSerializerCharField(source_field='job.User.id'),
        read_only=True
    )
    report = serializers.PrimaryKeyRelatedField(
        pk_field=HashidSerializerCharField(source_field='job.Report.id'),
        read_only=True
    )

    class Meta:
        model = models.Job
        exclude = []


class MutantSerializer(DynamicModelSerializer):
    id = HashidSerializerCharField(source_field='job.Mutant.id')
    job = serializers.PrimaryKeyRelatedField(
        pk_field=HashidSerializerCharField(source_field='job.Job.id'),
        read_only=True
    )

    class Meta:
        model = models.Mutant
        exclude = []
