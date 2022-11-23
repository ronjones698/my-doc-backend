from django.contrib import admin
from .models import AccountDetails,AuthAccount,user,PatientAccountDetails,Hospital,Company

admin.site.register(user)
admin.site.register(AccountDetails)
admin.site.register(AuthAccount)
admin.site.register(PatientAccountDetails)
admin.site.register(Hospital)
admin.site.register(Company)




