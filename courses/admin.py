from django.contrib import admin

from .models import Courses, LessonsBlock, Subthemes

admin.site.register(Courses)
admin.site.register(LessonsBlock)
admin.site.register(Subthemes)