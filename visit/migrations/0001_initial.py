# Generated by Django 3.2.7 on 2022-09-19 12:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_id', models.UUIDField(editable=False)),
                ('consultation_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('cost', models.IntegerField(default=0)),
                ('consultant', models.CharField(blank=True, max_length=50, null=True)),
                ('diagnosis', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Imaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_id', models.UUIDField(editable=False)),
                ('imaging_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('imager', models.CharField(blank=True, max_length=50, null=True)),
                ('cost', models.IntegerField(default=0)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('result', models.CharField(blank=True, max_length=50, null=True)),
                ('image_file_url', models.CharField(blank=True, max_length=50, null=True)),
                ('test', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_id', models.UUIDField(editable=False)),
                ('lab_tech', models.CharField(blank=True, max_length=50, null=True)),
                ('cost', models.IntegerField(default=0)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('result', models.CharField(blank=True, max_length=50, null=True)),
                ('facility', models.CharField(blank=True, max_length=50, null=True)),
                ('test', models.CharField(blank=True, max_length=50, null=True)),
                ('test_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_id', models.UUIDField(editable=False)),
                ('drug', models.CharField(blank=True, max_length=50, null=True)),
                ('prescriber', models.CharField(blank=True, max_length=50, null=True)),
                ('pharmacy_attendant', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('cost', models.IntegerField(default=0)),
                ('prescription_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('visit_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('patient_type', models.CharField(blank=True, max_length=50, null=True)),
                ('puporse', models.CharField(blank=True, max_length=50, null=True)),
                ('condition', models.CharField(blank=True, max_length=50, null=True)),
                ('outcome', models.CharField(blank=True, max_length=50, null=True)),
                ('facility_name', models.CharField(blank=True, max_length=50, null=True)),
                ('date_of_attendance', models.CharField(blank=True, max_length=50, null=True)),
                ('paitient_id', models.CharField(blank=True, max_length=50, null=True)),
                ('check_in_time', models.CharField(blank=True, max_length=50, null=True)),
                ('check_out_time', models.CharField(blank=True, max_length=50, null=True)),
                ('primary_diagnosis', models.CharField(blank=True, max_length=50, null=True)),
                ('secondary_diagnosis', models.CharField(blank=True, max_length=50, null=True)),
                ('procedure_code', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('hospital_id', models.CharField(max_length=50)),
                ('insurer_id', models.CharField(max_length=50)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
