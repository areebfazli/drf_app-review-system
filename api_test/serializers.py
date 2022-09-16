from dataclasses import field, fields
from rest_framework import serializers
from .models import Applicant


class ApplicantSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    age = serializers.IntegerField()
    qualification = serializers.CharField(max_length=500)
    gender = serializers.CharField(max_length=10)
    acceptance = serializers.NullBooleanField()

    class Meta:
        model = Applicant
        fields = ('__all__')