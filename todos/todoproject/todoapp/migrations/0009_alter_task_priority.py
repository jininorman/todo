# Generated by Django 4.2.4 on 2023-10-05 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0008_remove_task_description_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.PositiveIntegerField(default=0),
        ),
    ]