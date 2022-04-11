"""
views for lessons models
"""
from django.db import models
from courses.models import Courses, LessonsBlock, Subthemes



class Lesson(models.Model):
    """Class for Lessons"""
    lesson_name = models.CharField(
        max_length=250,
        verbose_name='Название занятия'
    )
    motivation = models.TextField(
        blank=True,
        verbose_name='Мотивация')
    actualization = models.TextField(
        blank=True,
        verbose_name='Актуализация')
    new_theme = models.TextField(
        blank=True,
        verbose_name='Новая тема')
    reflection = models.TextField(
        blank=True,
        verbose_name='Рефлексия')
    comments = models.TextField(
        blank=True,
        verbose_name='Комментарии')
    date_of_lesson = models.DateField(
        verbose_name='Дата занятия')
    course_id = models.ForeignKey(
       to=Courses,
        on_delete=models.PROTECT)
    group = models.CharField(
        max_length=150,
        verbose_name='Название группы')
    lessons_block_id = models.ForeignKey(
        to=LessonsBlock,
        on_delete=models.PROTECT)
    objects = models.Manager()


class LessonsList(models.Model):
    """Class for list of lessons"""
    date_of_lesson = models.DateField(
        verbose_name='Дата')
    lesson = models.TextField(
        blank=True,
        verbose_name='Урок')
    lessons_list = models.CharField(
        max_length=255,
        verbose_name='Список занятий')


class Glossary(models.Model):
    """Class for lessons list"""
    terms_blocks = models.CharField(
        max_length=250,
        verbose_name='Блок терминов')
    term = models.CharField(
        max_length=250,
        verbose_name='Термин')
    definition = models.TextField(
        blank=True,
        verbose_name='Определение')
    using = models.TextField(
        blank=True,
        verbose_name='Использование')
    lessons_id = models.ForeignKey(
        'Lesson',
        on_delete=models.PROTECT)
    subtheme_id = models.ForeignKey(
      to=Subthemes,
        on_delete=models.PROTECT)


class Hometasks(models.Model):
    """Class for hometasks"""
    date_of_hometasks = models.DateField(
        verbose_name='Дата')
    lessons_id = models.ForeignKey(
        'Lesson',
        on_delete=models.PROTECT)
    topics = models.CharField(
        max_length=250,
        verbose_name='Темы')
    task = models.TextField(
        blank=True,
        verbose_name='Задание')
    objects = models.Manager()


class Examination(models.Model):
    """Class for exams"""
    date_of_exam = models.DateField(
        verbose_name='Дата экзамена')
    recomendations = models.TextField(
        blank=True,
        verbose_name='Общие рекомендации')
    execution_time = models.DateField(

        verbose_name='Время выполнения')
    lessonsblock_id = models.ForeignKey(
       to=LessonsBlock,
        on_delete=models.PROTECT)
    task = models.TextField(
        blank=True,
        verbose_name='Задание')
    solved_task = models.TextField(
        blank=True,
        verbose_name='Решенное задание')
    results = models.IntegerField(
        blank=True,
        verbose_name='Результаты')
