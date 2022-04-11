"""Serializers for lessons module"""
from rest_framework.serializers import ModelSerializer
from .models import Hometasks, Lesson


class HometasksSerializer(ModelSerializer):
    """Class Serializer for hometasks"""
    class Meta:
        """fields"""
        model = Hometasks
        fields = '__all__'


class LessonsSerializer(ModelSerializer):
    """Class Serializer for lessons"""
    class Meta:
        """fields"""
        model = Lesson
        fields = '__all__'
