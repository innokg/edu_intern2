"""
Standart views.py for project
"""
from rest_framework.viewsets import ModelViewSet
from courses.serializers import CoursesSerializer, LessonsBlockSerializer, SubthemSerializer
from courses.models import Courses, LessonsBlock, Subthemes


class CourseViewSet(ModelViewSet):
    """Class for create and list courses"""
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class SubthemViewSet(ModelViewSet):
    """Class for create and list lesson blocks"""
    queryset = Subthemes.objects.all()
    serializer_class = SubthemSerializer


class LessonsBlockViewSet(ModelViewSet):
    """Class for create and list lesson blocks"""
    queryset = LessonsBlock.objects.all()
    serializer_class = LessonsBlockSerializer



