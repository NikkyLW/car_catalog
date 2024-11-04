from django.db import models
from django.urls import reverse
from users.models import User


class Car(models.Model):
    make = models.CharField(max_length=150, verbose_name='Марка')
    model = models.CharField(max_length=150, blank=True, verbose_name='Модель')
    year = models.CharField(max_length=150, blank=True, null=True, verbose_name='Год выпуска')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    created_at = models.DateTimeField(verbose_name='Дата и время записи', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата и время обновления', auto_now=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    
    class Meta:
        db_table = 'car'
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ("id",)

    def __str__(self):
        return f'{self.make} {self.model}'

    def display_id(self):
        return f"{self.id:05}"