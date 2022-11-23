# Generated by Django 3.2.7 on 2022-09-19 12:36

import Authentication.models
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('second_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('DOB', models.DateField(default=django.utils.timezone.now)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('account_type', models.CharField(blank=True, max_length=50, null=True)),
                ('organization_type', models.CharField(blank=True, max_length=50, null=True)),
                ('organization_name', models.CharField(blank=True, max_length=50, null=True)),
                ('user_type', models.CharField(blank=True, max_length=50, null=True)),
                ('identification_number', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AuthAccount',
            fields=[
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=50, null=True)),
                ('admin_email', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('telephone', models.CharField(blank=True, default='2547067454634', max_length=15, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('insurer_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DependentAccountDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('second_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('DOB', models.DateField(default=django.utils.timezone.now)),
                ('membership_id', models.CharField(blank=True, max_length=50, null=True)),
                ('relationship', models.CharField(blank=True, max_length=50, null=True)),
                ('insurer_id', models.CharField(max_length=50)),
                ('identification_number', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('admin_email', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('number_of_claims', models.IntegerField(default=0)),
                ('telephone', models.IntegerField(blank=True, default=2547067454634, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('hospital_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PatientAccountDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('second_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('DOB', models.DateField(default=django.utils.timezone.now)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('identification_number', models.CharField(blank=True, max_length=50, null=True)),
                ('membership_id', models.CharField(blank=True, max_length=50, null=True)),
                ('insurer_id', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50, unique=True, verbose_name='email')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', Authentication.models.UserManager()),
            ],
        ),
    ]