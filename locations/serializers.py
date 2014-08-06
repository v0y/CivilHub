# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.utils.translation import gettext as _
from django.contrib.contenttypes.models import ContentType
from .models import Location


class MapLocationSerializer(serializers.ModelSerializer):
    """
    Prosty serializer dla mapy. Przechowuje tylko podstawowe informacje o lo-
    kalizacji, czyli id, długość oraz szerokość geograficzną i typ zawartości
    (żeby sobie później ułatwić doczytywanie/segregowanie obiektów na mapie).
    Tylko zapytania typu GET! Serializers niejako sztucznie dopasowuje infor-
    macje o obiekcie na wzór obiektów z mapy (markerów), dając do dyspozycji
    ten sam szkielet modelu do Backbone.
    
    Umożliwia wyszukiwanie na podstawie kodu kraju (country_code), np:
    `?code=pl`
    zwróci wszystkie lokalizacje w Polsce.
    """
    id = serializers.Field(source='pk')
    content_type = serializers.SerializerMethodField('get_content_type')
    object_pk = serializers.Field(source='pk')

    def get_content_type(self, obj):
        return ContentType.objects.get_for_model(Location).pk

    class Meta:
        model = Location
        fields = ('id', 'latitude', 'longitude', 'content_type', 'object_pk',)


class SimpleLocationSerializer(serializers.ModelSerializer):
    """
    Simple location serializer for mobile API. Allows to list, add and manage
    location objects in database. Provides standard CRUD operations set.
    """
    class Meta:
        model = Location