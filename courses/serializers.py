from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from courses.models import Courses, LessonsBlock, Subthemes


class CoursesSerializer(ModelSerializer):

    class Meta:
        model = Courses
        fields = '__all__'


class LessonsBlockSerializer(ModelSerializer):

    class Meta:
        model = LessonsBlock
        fields = '__all__'


class SubthemSerializer(ModelSerializer):

    class Meta:
        model = Subthemes
        fields = '__all__'