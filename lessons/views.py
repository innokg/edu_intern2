"""
Views for lessons
"""
from rest_framework.viewsets import ModelViewSet
from lessons.serializers import HometasksSerializer, LessonsSerializer
from .models import Hometasks, Lesson


class HometaskViewSet(ModelViewSet):
    """Class for create and list Hometasks"""
    queryset = Hometasks.objects.all()
    serializer_class = HometasksSerializer


class LessonsViewSet(ModelViewSet):
    """Class for create and list Hometasks"""
    queryset = Lesson.objects.all()
    serializer_class = LessonsSerializer





