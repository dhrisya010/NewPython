# Generated by Django 3.2.16 on 2022-10-24 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='proirity',
            new_name='priority',
        ),
    ]
