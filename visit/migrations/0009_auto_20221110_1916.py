# Generated by Django 3.2.7 on 2022-11-10 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0008_alter_visit_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='consultation',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visit',
            name='laboratory',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visit',
            name='pharmacy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='visit',
            name='cost',
            field=models.IntegerField(default=0),
        ),
    ]