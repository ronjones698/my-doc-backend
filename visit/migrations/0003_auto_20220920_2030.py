# Generated by Django 3.2.7 on 2022-09-20 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0002_auto_20220919_1253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='hospital_id',
            new_name='hospital_name',
        ),
        migrations.RenameField(
            model_name='visit',
            old_name='insurer_id',
            new_name='insurer_name',
        ),
        migrations.RenameField(
            model_name='visit',
            old_name='paitient_id',
            new_name='paitient_name',
        ),
    ]
