from rest_framework import serializers
from .models import Visit,Prescription,Laboratory,Imaging,Consultation,FormScan

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = '__all__'

class ImagingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imaging
        fields = '__all__'

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'

class FormScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormScan
        fields = '__all__'