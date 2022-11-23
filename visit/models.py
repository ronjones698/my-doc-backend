from django.db import models
import uuid

class Visit(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    visit_id = models.CharField(max_length=50, null=True, blank=True) 
    patient_type = models.CharField(max_length=50, null=True, blank=True) 
    puporse = models.CharField(max_length=50, null=True, blank=True) 
    condition = models.CharField(max_length=50, null=True, blank=True)  
    outcome = models.CharField(max_length=50, null=True, blank=True) 
    facility_name = models.CharField(max_length=50, null=True, blank=True)
    date_of_attendance = models.CharField(max_length=50, null=True, blank=True)
    paitient_name = models.CharField(max_length=50, null=True, blank=True)
    paitient_id = models.CharField(max_length=50, null=True, blank=True)
    check_in_time = models.CharField(max_length=50, null=True, blank=True)
    check_out_time = models.CharField(max_length=50, null=True, blank=True)
    primary_diagnosis = models.CharField(max_length=50, null=True, blank=True)
    secondary_diagnosis = models.CharField(max_length=50, null=True, blank=True)
    procedure_code = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    hospital_name = models.CharField(max_length=50, null=False)
    insurer_name = models.CharField(max_length=50, null=False)
    status = models.CharField(max_length=50, null=False, default="visit")
    consultation = models.IntegerField(default=0)
    pharmacy = models.IntegerField(default=0)
    laboratory = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)

class FormScan(models.Model):
    visit_id = models.CharField(max_length=50, null=True, blank=True) 
    imageUrl = models.CharField(max_length=200, null=True, blank=True)


class Prescription(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    visit_id = models.CharField(max_length=50,null=True, blank=True) 
    drug = models.CharField(max_length=50, null=True, blank=True)
    prescriber = models.CharField(max_length=50, null=True, blank=True)
    pharmacy_attendant = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    cost =  models.IntegerField(default=0)
    prescription_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True) 

class Laboratory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    visit_id = models.CharField(max_length=50, null=True, blank=True) 
    lab_tech = models.CharField(max_length=50, null=True, blank=True)
    cost =  models.IntegerField(default=0)
    description = models.CharField(max_length=50, null=True, blank=True)
    result = models.CharField(max_length=50, null=True, blank=True)
    facility = models.CharField(max_length=50, null=True, blank=True)
    test = models.CharField(max_length=50, null=True, blank=True)
    test_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)

class Imaging(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    visit_id = models.CharField(max_length=50, null=True, blank=True) 
    imaging_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    imager = models.CharField(max_length=50, null=True, blank=True)
    cost =  models.IntegerField(default=0)
    description = models.CharField(max_length=50, null=True, blank=True)
    result = models.CharField(max_length=50, null=True, blank=True)
    image_file_url = models.CharField(max_length=50, null=True, blank=True)
    test = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Consultation(models.Model):
    visit_id = models.CharField(max_length=50, null=True, blank=True) 
    consultation_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    description = models.CharField(max_length=50, null=True, blank=True)
    cost =  models.IntegerField(default=0)
    consultant = models.CharField(max_length=50, null=True, blank=True)
    diagnosis = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)