# Generated by Django 4.0.5 on 2022-07-26 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='number_of_members',
        ),
    ]