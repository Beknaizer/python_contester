# Generated by Django 3.1.7 on 2021-04-30 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contester', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_definitoin',
            new_name='task_definition',
        ),
    ]