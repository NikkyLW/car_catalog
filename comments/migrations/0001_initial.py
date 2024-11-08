# Generated by Django 4.2.7 on 2024-10-31 02:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0004_rename_cars_car_alter_car_options_alter_car_table'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время комментария')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.car', verbose_name='Автомобиль')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'db_table': 'comment',
                'ordering': ('id',),
            },
        ),
    ]
