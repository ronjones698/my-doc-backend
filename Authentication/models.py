from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
import uuid


class UserManager(BaseUserManager):
    use_in_migrations = True
    def save_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None,**extra_fields):
        extra_fields['is_superuser'] = False
        extra_fields['is_staff'] = False
        return self.save_user(email, password)

    def create_staffuser(self, email, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = False
        return self.save_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
                raise ValueError('is_superuser should be True')
        extra_fields['is_staff'] = True
        return self.save_user(email, password, **extra_fields)

class user(AbstractBaseUser,PermissionsMixin):
    id = models.BigAutoField(
        primary_key = True,
    )
    email = models.CharField(
        max_length = 50, 
        unique = True, 
        verbose_name = "email"
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    objects = UserManager()

class AuthAccount(models.Model):
    email = models.EmailField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)

class AccountDetails(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True) 
    second_name = models.CharField(max_length=50, null=True, blank=True) 
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    DOB = models.DateField(default=timezone.now)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    account_type = models.CharField(max_length=50, null=True, blank=True)
    organization_type = models.CharField(max_length=50, null=True, blank=True)
    organization_name = models.CharField(max_length=50, null=True, blank=True)
    user_type = models.CharField(max_length=50, null=True, blank=True)
    identification_number = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    imageUrl = models.CharField(max_length=1500, null=True, blank=True)

class PatientAccountDetails(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True) 
    second_name = models.CharField(max_length=50, null=True, blank=True) 
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    DOB = models.DateField(default=timezone.now)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    identification_number = models.CharField(max_length=50, null=True, blank=True)
    membership_id = models.CharField(max_length=50, null=True, blank=True)
    insurer_id = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    relationship = models.CharField(max_length=50, null=True, blank=True)

class DependentAccountDetails(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True) 
    second_name = models.CharField(max_length=50, null=True, blank=True) 
    last_name = models.CharField(max_length=50, null=True, blank=True)
    DOB = models.DateField(default=timezone.now)
    membership_id = models.CharField(max_length=50, null=True, blank=True)
    relationship = models.CharField(max_length=50, null=True, blank=True)
    insurer_id = models.CharField(max_length=50, null=False)
    identification_number = models.CharField(max_length=50, null=True, blank=True)


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=50, null=True, unique=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    admin_email = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    number_of_claims = models.IntegerField(default=0)
    telephone = models.IntegerField(default=2547067454634, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    hospital_id = models.CharField(max_length=50, null=False)
    imageUrl = models.CharField(max_length=1500, null=True, blank=True)

class Company(models.Model):
    company_name = models.CharField(max_length=50, null=True, blank=True)
    admin_email = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True) 
    email = models.EmailField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    telephone = models.CharField(default="2547067454634",max_length=15, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    insurer_id = models.CharField(max_length=50, null=False)
    imageUrl = models.CharField(max_length=1500, null=True, blank=True)

