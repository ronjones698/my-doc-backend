# Generated by Django 3.2.7 on 2022-09-27 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0005_visit_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='status',
            field=models.CharField(default='pending', max_length=50),
        ),
    ]
