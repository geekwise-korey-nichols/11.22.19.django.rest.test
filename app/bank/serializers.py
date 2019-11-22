from bank.models import Branch
from rest_framework import serializers


class Branch_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branch
        fields = ['location_name', 'location', 'location_id']

