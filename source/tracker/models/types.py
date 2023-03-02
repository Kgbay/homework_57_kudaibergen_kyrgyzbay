from django.db import models
from django.db.models import TextChoices


class TypeChoice(TextChoices):
    TASK = ('Task', 'Задача')
    BUG = ('Bug', 'Ошибка')
    ENHANCEMENT = ('Enhancement', 'Задача')


class Type(models.Model):
    type_name = models.CharField(
        max_length=30,
        null=False,
        choices=TypeChoice.choices,
        verbose_name='Наименование типа')

    def __str__(self):
        return f"{self.type_name}"
