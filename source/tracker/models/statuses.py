from django.db import models
from django.db.models import TextChoices


class StatusChoice(TextChoices):
    NEW = ('New', 'Новый')
    IN_PROGRESS = ('In progress', 'В процессе')
    DONE = ('Done', 'Выполнено')

class Status(models.Model):
    status_name = models.CharField(
        max_length=30,
        choices=StatusChoice.choices,
        null=False,
        verbose_name='Наименование статуса')

    def __str__(self):
        return f"{self.status_name}"
