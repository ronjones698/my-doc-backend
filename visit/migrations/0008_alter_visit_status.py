# Generated by Django 3.2.7 on 2022-09-29 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0007_formscan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='status',
            field=models.CharField(default='visit', max_length=50),
        ),
    ]