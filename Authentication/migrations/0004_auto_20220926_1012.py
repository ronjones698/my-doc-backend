# Generated by Django 3.2.7 on 2022-09-26 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0003_accountdetails_imageurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='imageUrl',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='imageUrl',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
    ]
