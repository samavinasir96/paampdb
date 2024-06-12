from rest_framework import serializers
from abampdb.models import Proteins, Docks


class ProteinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proteins
        fields = ('amp', 'name', 'pdb_name')


class DocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docks
        fields = ('dock_1', 'name')
        