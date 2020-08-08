from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(DoctorRegister)
admin.site.register(DoctorDatabase)
admin.site.register(PatientRegister)
admin.site.register(PatientDatabase)
admin.site.register(Appointment)
admin.site.register(ReceptionistRegister)
admin.site.register(ReceptionistDatabase)
admin.site.register(HRRegister)
admin.site.register(HRDatabase)