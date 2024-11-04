from django.db import models
from django.urls import reverse
from cars.models import Car
from users.models import User


class Comment(models.Model):
    content = models.TextField(blank=True, null=True, verbose_name='Описание')
    created_at = models.DateTimeField(verbose_name='Дата и время комментария', auto_now_add=True)
    car = models.ForeignKey(to=Car, on_delete=models.CASCADE, verbose_name='Автомобиль', blank=True, null=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    
    class Meta:
        db_table = 'comment'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ("id",)

    def __str__(self):
        return f'{self.content}'

    def display_id(self):
        return f"{self.id:05}"