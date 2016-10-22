from rest_framework import serializers

from .models import Hospital

HOSPITAL_FIELDS = ('id',
                   'created',
                   'name',
                   'latitude',
                   'longitude',
                   'contact',
                   'address',
                   'business_hours')


class HospitalSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model  = Hospital
        fields = HOSPITAL_FIELDS
