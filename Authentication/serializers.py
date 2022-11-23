from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import user,AuthAccount,AccountDetails,PatientAccountDetails,DependentAccountDetails,Hospital,Company

class AuthAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthAccount
        fields = '__all__'

class AuthTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.email
        return token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ("id","email","password")
        extra_kwargs = {'password': {'write_only': True}}

class AccountDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountDetails
        fields = '__all__'

class PatientAccountDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientAccountDetails
        fields = '__all__'

class DependentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DependentAccountDetails
        fields = '__all__'

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'    