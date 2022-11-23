from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Visit,Prescription,Laboratory,Imaging,Consultation,FormScan
from .serializer import VisitSerializer,PrescriptionSerializer,LaboratorySerializer,ImagingSerializer,ConsultationSerializer,FormScanSerializer
from Authentication.models import AccountDetails,Hospital,Company,DependentAccountDetails,PatientAccountDetails
import uuid
import requests
import random

char_array = ['A',"B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def generate_visit_id():
    visit_id = ""
    for i in range(3):
        visit_id += char_array[random.randint(0,25)]
    visit_id = visit_id + "-" + f'{random.randrange(1, 10**3):03}'
    return visit_id

print(generate_visit_id())

class VisitView(viewsets.ViewSet):
    serializer_class = VisitSerializer

    def successfully_updated_status(self,status,dbobject):
        updated_instance = {"status":status}
        serializer_instance = VisitSerializer(dbobject,data=updated_instance,partial=True)
        if(serializer_instance.is_valid()):
            serializer_instance.save()
            return True
        return False

    def convert_to_uuid(self,data,field):
        data[field] = uuid.UUID(data[field])
        return data

    @action(detail=False,methods=['POST'])
    def add_visit(self,request):
        data = JSONParser().parse(request)
        try:
            Patient = AccountDetails.objects.filter(identification_number=data["patient_id"])[0]
        except:
            return Response({"Success":False,"Message":"Incorrect user identification"})
        
        if(Patient.account_type != "Patient"):
            return Response({"Success":False,"Message":"This user is not a patient"})
        if(Patient.user_type == "Dependent"):
            patient_data = DependentAccountDetails.objects.filter(identification_number=Patient.identification_number)[0]
        elif(Patient.user_type == "Patient"):
            patient_data = PatientAccountDetails.objects.filter(identification_number=Patient.identification_number)[0]
        try:
            Agent_account = AccountDetails.objects.filter(email=data["agent_email"])[0]
        except:
            return Response({"Success":False,"Message":"You are not permited to use this service"})
        if(Agent_account.user_type != "Reception" or Agent_account.organization_type != "Hospital"):
            return Response({"Success":False,"Message":"This route is only open to Hospital receptionists"})
        try:
            insurer = Company.objects.filter(insurer_id=patient_data.insurer_id)[0]
        except:
            return Response({"Success":False,"Message":"Insurer not found"})
        data["insurer_name"] = insurer.company_name
        data["visit_id"] = generate_visit_id()
        data["hospital_name"] = data["facility_name"]
        data["paitient_id"] = data["patient_id"]
        data["paitient_name"] = f"{patient_data.first_name} {patient_data.second_name}"
        data["imageUrl"] = "http://127.0.0.1:5000/static/uploads/" + Patient.imageUrl
        serializer = self.serializer_class(data=data,context={'request': request})
        if(serializer.is_valid()):
            serializer.save()
            facerec = requests.post("http://127.0.0.1:5000/recieve_visit_details/", json=data)
            return Response({"Success":True,"Message":"Visit added successfully"})
        return Response(serializer.errors)
    @action(detail=True,methods=['POST'])
    def update_visit(self,request,pk):
        data = JSONParser().parse(request)
        try:
            visit_object = Visit.objects.filter(visit_id=pk)[0]
        except:
            return Response({"Success":False,"Message":"Visit was not found"})
        visit_serializer = VisitSerializer(visit_object,data=data,partial=True,context={'request': request})
        if(visit_serializer.is_valid()):
            visit_serializer.save()
            return Response({"Success":True,"Message":"Form has been updated"})
        return Response(visit_serializer.errors)
        
    @action(detail=True,methods=['POST'])
    def update_visit_status(self,request,pk):
        data = JSONParser().parse(request)
        try:
            visit_object = Visit.objects.filter(visit_id=pk)[0]
        except:
            return Response({"Success":False,"Message":"Visit was not found"})
        visit_serializer = VisitSerializer(visit_object,data=data,partial=True,context={'request': request})
        if(visit_serializer.is_valid()):
            visit_serializer.save()
            return Response({"Success":True,"Message":"Claim has been updated"})
        return Response(visit_serializer.errors)

    @action(detail=False,methods=['GET'])
    def get_all_visits(self,request):
        queryset = Visit.objects.all()
        serializer = VisitSerializer(data=list(queryset.values()),many=True,context={'request':request})
        return Response(serializer.initial_data)

    @action(detail=True,methods=['GET'])
    def get_visit_by_id(self,request,pk):
        queryset = Visit.objects.filter(visit_id=pk).values()
        try:
            data =  VisitSerializer(data=queryset[0],many=False,context={'request':request})
            resp_data = data.initial_data
        except:
            return Response({"Success":False,"Message":"Visit not found"})
        if(PatientAccountDetails.objects.filter(identification_number=resp_data["paitient_id"])):
            user = PatientAccountDetails.objects.filter(identification_number=resp_data["paitient_id"])[0]
        else:
            user = DependentAccountDetails.objects.filter(identification_number=resp_data["paitient_id"])[0]
        user_details = AccountDetails.objects.filter(identification_number=resp_data["paitient_id"])[0]
        resp_data["first_name"] = user.first_name
        resp_data["second_name"] = user.second_name
        resp_data["membership_id"] = user.membership_id
        resp_data["relationship"] = user.relationship
        resp_data["imageUrl"] = user_details.imageUrl
        return Response(resp_data)

    @action(detail=True,methods=['GET'])
    def get_hospital_visits(self,request,pk):
        try:
            company = Company.objects.filter(company_name=pk)[0]
            queryset = Visit.objects.filter(insurer_name=pk)
        except:
            queryset = Visit.objects.filter(hospital_name=pk)
        serializer = VisitSerializer(data=list(queryset.values()),many=True,context={'request':request})
        return Response(serializer.initial_data)

    @action(detail=True,methods=['GET'])
    def get_hospital_id_visits(self,request,pk):
        try:
            company = Company.objects.filter(insurer_id=pk)[0]
            queryset = Visit.objects.filter(insurer_name=company.company_name)
        except:
            hospital = Hospital.objects.filter(hospital_id=pk)[0]
            queryset = Visit.objects.filter(hospital_name=hospital.hospital_name)
        serializer = VisitSerializer(data=list(queryset.values()),many=True,context={'request':request})
        return Response(serializer.initial_data)  

    @action(detail=False,methods=['POST'])
    def add_prescription(self,request):
        data = JSONParser().parse(request)
        try:
            visit = Visit.objects.filter(visit_id=data["visit_id"])[0]
            current_cost = data["cost"]
            data["pharmacy"] = visit.pharmacy + data["cost"]
            data["cost"] = visit.cost + data["cost"]
            Visit_serializer_instance = VisitSerializer(visit,data=data,partial=True,context={"request":request})
            if(Visit_serializer_instance.is_valid()):
                Visit_serializer_instance.save()
            else:
                return Response(Visit_serializer_instance.errors)
        except:
            return Response({"Success":False,"Message":"The visit id given is not recorded"})
        try:
            Agent_account = AccountDetails.objects.filter(email=data["agent_email"])[0]
        except:
            return Response({"Success":False,"Message":"Agent not recognized"})
        if(Agent_account.user_type != "doctor" or Agent_account.organization_type != "Hospital" ):
            return Response({"Success":False,"Message":"This route is only open to doctors"})
        data["cost"] = current_cost
        Prescription_serializer_instance = PrescriptionSerializer(data=data)
        if(Prescription_serializer_instance.is_valid() and self.successfully_updated_status("Pharmacy",visit)):
            Prescription_serializer_instance.save()
            return Response({"Success":True,"Message":"Prescription added successfully"})

        return Response(Prescription_serializer_instance.errors)

    @action(detail=True,methods=['GET'])
    def get_prescriptions(self,request,pk):
        visit_queryset = Prescription.objects.filter(visit_id=pk).values()
        Prescription_serializer_instance = PrescriptionSerializer(data=list(visit_queryset),many=True,context={'request':request})
        return Response(Prescription_serializer_instance.initial_data)

    @action(detail=False,methods=['POST'])
    def add_lab_test(self,request):
        data = JSONParser().parse(request)
        try:
            visit = Visit.objects.filter(visit_id=data["visit_id"])[0]
            current_cost = data["cost"]
            data["laboratory"] = visit.laboratory + data["cost"]
            data["cost"] = visit.cost + data["cost"]
            Visit_serializer_instance = VisitSerializer(visit,data=data,partial=True,context={"request":request})
            if(Visit_serializer_instance.is_valid()):
                Visit_serializer_instance.save()
            else:
                return Response(Visit_serializer_instance.errors)
        except:
            return Response({"Success":False,"Message":"The visit id given is not recorded"})
        try:
            Agent_account = AccountDetails.objects.filter(email=data["agent_email"])[0]
        except:
            return Response({"Success":False,"Message":"Agent not recognized"})
        if(Agent_account.user_type != "doctor" or Agent_account.organization_type != "Hospital" ):
            return Response({"Success":False,"Message":"This route is only open to doctors"})
        data["cost"] = current_cost
        Laboratory_serializer_instance = LaboratorySerializer(data=data)
        if(Laboratory_serializer_instance.is_valid() and self.successfully_updated_status("Laboratory",visit)):
            Laboratory_serializer_instance.save()
            return Response({"Success":True,"Message":"Test added successfully"})

        return Response(Laboratory_serializer_instance.errors)

    @action(detail=True,methods=['GET'])
    def get_lab_tests(self,request,pk):
        visit_queryset = Laboratory.objects.filter(visit_id=pk).values()
        Prescription_serializer_instance = LaboratorySerializer(data=list(visit_queryset),many=True,context={'request':request})
        return Response(Prescription_serializer_instance.initial_data)

    @action(detail=False,methods=['POST'])
    def add_imaging_test(self,request):
        data = JSONParser().parse(request)
        try:
            visit = Visit.objects.filter(visit_id=data["visit_id"])[0]
            current_cost = data["cost"]
            data["cost"] = visit.cost + data["cost"]
            Visit_serializer_instance = VisitSerializer(visit,data=data,partial=True,context={"request":request})
            if(Visit_serializer_instance.is_valid()):
                Visit_serializer_instance.save()
            else:
                return Response(Visit_serializer_instance.errors)

        except:
            return Response({"Success":False,"Message":"The visit id given is not recorded"})
        try:
            Agent_account = AccountDetails.objects.filter(email=data["agent_email"])[0]
        except:
            return Response({"Success":False,"Message":"Agent not recognized"})
        if(Agent_account.user_type != "doctor" or Agent_account.organization_type != "Hospital" ):
            return Response({"Success":False,"Message":"This route is only open to doctors"})
        data["cost"] = current_cost
        Imaging_serializer_instance = ImagingSerializer(data=data)
        if(Imaging_serializer_instance.is_valid() and self.successfully_updated_status("Imaging",visit)):
            Imaging_serializer_instance.save()
            return Response({"Success":True,"Message":"Scan added successfully"})
        return Response(Imaging_serializer_instance.errors)

    @action(detail=True,methods=['GET'])
    def get_Imaging_tests(self,request,pk):
        visit_queryset = Imaging.objects.filter(visit_id=pk).values()
        Prescription_serializer_instance = ImagingSerializer(data=list(visit_queryset),many=True,context={'request':request})
        return Response(Prescription_serializer_instance.initial_data)

    @action(detail=False,methods=['POST'])
    def add_consultation(self,request):
        data = JSONParser().parse(request)
        try:
            visit = Visit.objects.filter(visit_id=data["visit_id"])[0]
            current_cost = data["cost"]
            data["consultation"] = visit.consultation + data["cost"]
            data["cost"] = visit.cost + data["cost"]
            Visit_serializer_instance = VisitSerializer(visit,data=data,partial=True,context={"request":request})
            if(Visit_serializer_instance.is_valid()):
                Visit_serializer_instance.save()
            else:
                return Response(Visit_serializer_instance.errors)
        except:
            return Response({"Success":False,"Message":"The visit id given is not recorded"})
        try:
            Agent_account = AccountDetails.objects.filter(email=data["agent_email"])[0]
        except:
            return Response({"Success":False,"Message":"Agent not recognized"})
        if(Agent_account.user_type != "doctor" or Agent_account.organization_type != "Hospital" ):
            return Response({"Success":False,"Message":"This route is only open to doctors"})
        data["cost"] = current_cost
        Consultation_serializer_instance = ConsultationSerializer(data=data)
        if(Consultation_serializer_instance.is_valid() and self.successfully_updated_status("Consultation",visit)):
            Consultation_serializer_instance.save()
            return Response({"Success":True,"Message":"Consultation added successfully"})
        return Response(Consultation_serializer_instance.errors)

    @action(detail=True,methods=['GET'])
    def get_consultation(self,request,pk):
        visit_queryset = Consultation.objects.filter(visit_id=pk).values()
        Prescription_serializer_instance = ConsultationSerializer(data=visit_queryset[0],many=False,context={'request':request})
        return Response(Prescription_serializer_instance.initial_data)


class FormScanView(viewsets.ModelViewSet):
    queryset = FormScan.objects.all()
    serializer_class = FormScanSerializer

    @action(detail=True,methods=['GET'])
    def get_form_scans(self,request,pk):
        form_queryset = FormScan.objects.filter(visit_id=pk).values()
        form_scan_serializer = self.serializer_class(data=form_queryset,many=True,context={'request':request})
        return Response(form_scan_serializer.initial_data)