"""
standart models for educational project
"""


from django.db import models
from rest_framework.reverse import reverse


class Courses(models.Model):
    """Class for courses"""
    title_of_courses = models.CharField(
        max_length=150,
        verbose_name='Название курса',
        unique=True)
    description_of_courses = models.TextField(
        verbose_name='Описание курса')
    dates_of_event = models.DateField(
        verbose_name='Дата проведения')
    mentor = models.CharField(
        max_length=255,
        verbose_name='Ментор')
    subthemes_id = models.ForeignKey(
        'Subthemes',
        on_delete=models.PROTECT,
        verbose_name='Подтемы',
        blank=True, null=True)
    lessons_block_id = models.ForeignKey(
        'LessonsBlock',
        on_delete=models.PROTECT,
        verbose_name='Блок занятий',
        blank=True, null=True)
    lessons_list_id = models.ForeignKey(
        to="lessons.LessonsList",
        on_delete=models.PROTECT,
        verbose_name='Список уроков',
        blank=True, null=True)
    hometasks_list_id = models.ForeignKey(
        to="lessons.LessonsList",
        on_delete=models.PROTECT,
        verbose_name='Список ДЗ',
        related_name='tasks',
        blank=True, null=True)
    course_completion_rate = models.IntegerField(
        blank=True,
        verbose_name='Процент освоения темы')
    objects = models.Manager()

    def __str__(self):
        return self.title_of_courses


class Subthemes(models.Model):
    """Class for subthemes of courses"""
    subtheme_title = models.CharField(
        max_length=255,
        verbose_name='Название подтемы')
    lessons_id = models.ForeignKey(
        to="lessons.Lesson",
        blank=True, null=True,
        on_delete=models.PROTECT)
    comments = models.TextField(
        blank=True,
        verbose_name='Комментарии')
    lessons_block_id = models.ForeignKey(
        'LessonsBlock',
        blank=True, null=True,
        on_delete=models.PROTECT)
    objects = models.Manager()

    def __str__(self):
        return self.subtheme_title

    def get_absolute_url(self):
        return reverse('subthemes', kwargs={'pk': self.pk})

class LessonsBlock(models.Model):
    """Class for block of lessons"""
    number_of_lessons = models.IntegerField(
        unique=True,
        verbose_name='Номер блока')
    lessons_title = models.CharField(
        max_length=250,
        verbose_name='Название блока')
    goals_at_the_end = models.TextField(
        blank=True,
        verbose_name='Цель по окончании')
    objects = models.Manager()

    def __str__(self):
        return self.lessons_title
