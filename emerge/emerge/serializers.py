from rest_framework import serializers
from .models        import Hospital

HOSPITAL_FIELDS = ('id',
                   'created',
                   'name',
                   'latitude',
                   'longitude',
                   'contact',
                   'address',
                   'business_hours')


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    created = serializers.ReadOnlyField(source='created')
    id      = serializers.ReadOnlyField(source='id')

    class Meta:
        model  = Hospital
        fields = HOSPITAL_FIELDS
