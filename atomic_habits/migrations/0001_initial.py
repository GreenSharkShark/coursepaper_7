# Generated by Django 4.2.5 on 2023-09-21 08:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=250, verbose_name='место')),
                ('time', models.DateTimeField(verbose_name='время')),
                ('action', models.TextField(verbose_name='действие')),
                ('is_pleasant_habit', models.BooleanField(default=False, verbose_name='признак приятной привычки')),
                ('is_related_habit', models.BooleanField(default=False, verbose_name='признак связанной привычки')),
                ('periodicity', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(7)], verbose_name='периодичность в днях')),
                ('award', models.CharField(max_length=250, verbose_name='награда')),
                ('time_to_complete', models.PositiveSmallIntegerField(default=60, validators=[django.core.validators.MaxValueValidator(120)], verbose_name='время на выполнение')),
                ('is_published', models.BooleanField(default=False, verbose_name='признак публичности')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habit', to=settings.AUTH_USER_MODEL, verbose_name='создатель привычки')),
            ],
        ),
    ]
