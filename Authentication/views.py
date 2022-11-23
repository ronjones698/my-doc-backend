from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import AuthAccount,AccountDetails,user,PatientAccountDetails,DependentAccountDetails,Hospital,Company
from .serializers import (TokenObtainPairSerializer,DependentDetailsSerializer,AccountDetailsSerializer,
                          AuthAccountSerializer,UserSerializer,PatientAccountDetailsSerializer,
                          HospitalSerializer,CompanySerializer)
import uuid

class UsersView(viewsets.ViewSet):
    serializer_class = UserSerializer

    @action(detail=False,methods=['POST'])
    def register(self, request):
        data = JSONParser().parse(request)
        try:
            user_type = data['user_type']
        except:
            return Response({"Success":False,"Message":"Enter the usertype"})

        if(data["account_type"] == "Patient"):
            Agent_account = AccountDetails.objects.filter(email=data["agent_email"])[0]
            if(Agent_account.organization_name != data["organization_name"]):
                return Response({"Success":"False","Message":"You are not allowed to add a user"})
        elif(data["organization_type"] == "Insurance"):
            try:
                company = Company.objects.filter(admin_email=data["agent_email"])[0]
            except:
                return Response({"Success":False,"Message":"You are not allowed to add this user"})
        elif(data["organization_type"] == "Hospital"):
           try:
                hospital = Hospital.objects.filter(admin_email=data["agent_email"])[0]
           except:
                return Response({"Success":False,"Message":"You are not allowed to add this user"})

        else:
            return Response({"Success":False,"Message":"Please Enter the correct account type"})
        try:
           if(Hospital.objects.filter(hospital_name=data["organization_name"])):
               organization_account = Hospital.objects.filter(hospital_name=data["organization_name"])[0]
           else:
               organization_account = Company.objects.filter(company_name=data["organization_name"])[0]
        except:
            return Response({"Success":False,"Message":"Organization not found"})

        if(user_type == 'Dependent'):
            try:
                insurer = Company.objects.filter(company_name=data["insurer"])[0]
            except:
                return Response({"Success":False,"Message":"Insurer not found"})
            data["insurer_id"] = insurer.insurer_id
            if(len(Hospital.objects.filter(hospital_name=data["organization_name"])) == 0 and len(Company.objects.filter(company_name=data["organization_name"])) == 0):
                return Response({"Success":False,"Message":"Otganization does not exist"})
            if(Agent_account.organization_name != data["organization_name"] and Agent_account.organization_name != data["organization_name"]):
                return Response({"Success":"False","Message":"You are not allowed to add a user"})
                
            if(Agent_account.user_type == "Claims" or Agent_account.user_type == "admin"):    
                if(PatientAccountDetails.objects.filter(membership_id=data["membership_id"])):
                    if(DependentAccountDetails.objects.filter(identification_number=data["identification_number"])):
                        return Response({"Success":False,"Message":"Dependent already exists"})
                    dependent_account_serializer = DependentDetailsSerializer(data=data,context={'request': request})
                    account_details_serializer = AccountDetailsSerializer(data=data,context={'request': request})
                    if(dependent_account_serializer.is_valid() and account_details_serializer.is_valid()):
                        dependent_account_serializer.save()
                        account_details_serializer.save()
                        return Response({"Success":True,"Message":"Dependent added successfully"})
                    return Response({"Success":False,"Errors":[dependent_account_serializer.errors,account_details_serializer.errors]})
                return Response({"Success":False,"Message":"Membership id does not exist"})
            return Response({"Success":"False","Message":"You are not allowed to add a user"})

        if(user_type == 'Patient'):
            try:
                insurer = Company.objects.filter(company_name=data["insurer"])[0]
            except:
                return Response({"Success":False,"Message":"Insurer not found"})
            data["insurer_id"] = insurer.insurer_id
            if(Hospital.objects.filter(hospital_name=data["organization_name"]) == 0 and len(Company.objects.filter(company_name=data["organization_name"]) == 0)):
                return Response({"Success":False,"Message":"Organization does not exist"})
            if(Agent_account.organization_name != data["organization_name"] and Agent_account.organization_name != data["organization_name"]):  
                return Response({"Success":"False","Message":"You are h not allowed to add a user"})
            if(Agent_account.user_type == "Claims" or Agent_account.user_type == "admin"):
                if(PatientAccountDetails.objects.filter(identification_number=data["identification_number"]) or PatientAccountDetails.objects.filter(membership_id=data["membership_id"])):
                    return Response({"Success":False,"Message":"User already exists"})
                patient_serializer = PatientAccountDetailsSerializer(data=data,context={'request': request})
                account_details_serializer = AccountDetailsSerializer(data=data,context={'request': request})
                if(patient_serializer.is_valid() and account_details_serializer.is_valid()):
                    patient_serializer.save()
                    account_details_serializer.save()
                    return Response({"Success":True,"Message":"Patient Added Successfully"})
                return Response({"Success":False,"Errors":[patient_serializer.errors,account_details_serializer.errors]})
            return Response({"Success":"False","Message":"You are not allowed to add a user"}) 

        if(AccountDetails.objects.filter(email=data["email"])):
            return Response({"Success":False,"Message":"User already exists"})
        if(data["user_type"] == "admin"):
            if(organization_account.admin_email != data["email"]):
                return Response({"Success":False,"Message":"The email provided is not the organization's registered email adrress"})
        
        account_details_serializer = AccountDetailsSerializer(data=data,context={'request': request})
        registered_user = user.objects.create_user(data["email"],data["password"])
        if(account_details_serializer.is_valid()):
            if(registered_user):
                account_details_serializer.save()
                return Response({"Success":True,"Message":"User created successfully"})
            return Response({"Success":True,"Message":"Could not register user"})
        return Response(account_details_serializer.errors)


    @action(detail=True,methods=['GET'])
    def get_users(self, request,pk):
        queryset = AccountDetails.objects.filter(organization_name=pk)
        serializer = AccountDetailsSerializer(data=list(queryset.values()),many=True,context={'request':request})
        return Response(serializer.initial_data)

    @action(detail=True,methods=['GET'])
    def get_user(self,request,pk):
        try:
            queryset = AccountDetails.objects.filter(identification_number=pk).values()
            serializer = AccountDetailsSerializer(data=queryset[0],many=False,context={'request':request})
            return Response({"Success":True,"Message":serializer.initial_data})
        except:
            return Response({"Success":False,"Message":"User not found"})
        

    @action(detail=True,methods=['GET'])
    def get_user_by_email(self,request,pk):
        pk += ".com"
        try:
            queryset = AccountDetails.objects.filter(email=pk).values()
            serializer = AccountDetailsSerializer(data=queryset[0],many=False,context={'request':request})
            return Response({"Success":True,"Message":serializer.initial_data})
        except:
            return Response({"Success":False,"Message":"User not found"})


    @action(detail=False,methods=['GET'])
    def get_all_users(self, request):
        queryset = AccountDetails.objects.all()
        serializer = AccountDetailsSerializer(data=list(queryset.values()),many=True,context={'request':request})
        return Response(serializer.initial_data)

    @action(detail=False,methods=['GET'])
    def get_patients(self, request):
        queryset = PatientAccountDetails.objects.all()
        serializer = PatientAccountDetailsSerializer(data=list(queryset.values()),many=True,context={'request':request})
        return Response(serializer.initial_data)

    @action(detail=True,methods=['GET'])
    def get_patient(self, request,pk):
        patients_queryset = PatientAccountDetails.objects.filter(identification_number=pk)
        dependent_queryset = DependentAccountDetails.objects.filter(identification_number=pk)
        if(patients_queryset):
            patients_serializer = PatientAccountDetailsSerializer(data=patients_queryset.values()[0],many=False,context={"request":request})
        elif(dependent_queryset):
            patients_serializer = DependentDetailsSerializer(data=dependent_queryset.values()[0],many=False,context={"request":request})
        else:
            return Response({"Success":False,"Message":"Patient does not exist"})
        return Response(patients_serializer.initial_data)


class HospitalView(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

    @action(detail=True,methods=['GET'])
    def get_hospital(self,request,pk):
        try:
            queryset = Hospital.objects.filter(hospital_id=pk).values()
            serializer = HospitalSerializer(data=queryset[0],many=False,context={'request':request})
            return Response({"Success":True,"Message":serializer.initial_data})
        except:
            return Response({"Success":False,"Message":"User not found"})

class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
