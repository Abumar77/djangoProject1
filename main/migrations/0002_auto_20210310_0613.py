# Generated by Django 3.1.7 on 2021-03-10 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='text',
            new_name='task',
        ),
    ]