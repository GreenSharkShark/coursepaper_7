# Generated by Django 4.2.5 on 2023-09-23 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atomic_habits', '0004_habit_related_habit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='is_related_habit',
        ),
    ]
