from django.db import models
from django.db.models.signals import post_save
import datetime
# Create your models here.

# this class is used for creating a model for registration form of doctor
class DoctorRegister(models.Model):

    username = models.CharField(
        max_length=50
    )

    password = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.username

# this class is used for creating other details of doctor
class DoctorDatabase(models.Model):

    CHOICE1=(
        ("Allergists", "Allergists"),
        ("Dermatologists", "Dermatologists"),
        ("Ophthalmologists", "Ophthalmologists"),
        ("Gynecologists", "Gynecologists"),
        ("Cardiologists", "Cardiologists"),
        ("Endocrinologists", "Endocrinologists"),
        ("Gastroenterologists", "Gastroenterologists"),
        ("Nephrologists", "Nephrologists"),
        ("Urologists", "Urologists"),
        ("Pulmonologists", "Pulmonologists"),
        ("Otolaryngologists", "Otolaryngologists"),
        ("Neurologists", "Neurologists"),
        ("Psychiatrists", "Psychiatrists"),
        ("Oncologists", "Oncologists"),
        ("Radiologists", "Radiologists"),
        ("Rheumatologists", "Rheumatologists"),
        ("General surgeons", "General surgeons"),
        ("Orthopedic surgeons", "Orthopedic surgeons"),
        ("Cardiac surgeons", "Cardiac surgeons"),
        ("Anesthesiologists", "Anesthesiologists")
    )

    CHOICE2 = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")
    )

    userInstance = models.OneToOneField(
        DoctorRegister,
        on_delete=models.CASCADE
    )

    firstname = models.CharField(
        max_length=50
    )

    lastname = models.CharField(
        max_length=50
    )

    speciality = models.CharField(
        max_length=50,
        choices=CHOICE1
    )

    address = models.CharField(
        max_length=500
    )

    emailID = models.EmailField(
        max_length=200
    )

    phone = models.CharField(
        max_length=10,
    )

    gender = models.CharField(
        max_length=30,
        choices=CHOICE2
    )

    def __str__(self):
        return str(self.firstname + " " + self.lastname + " " + self.emailID)

def create_profile(sender, instance, created, **kwargs):
    if created:
        DoctorDatabase.objects.create(userInstance=instance)

post_save.connect(create_profile, sender=DoctorRegister)


# this class is used for creating patient registration form
class PatientRegister(models.Model):

    username = models.CharField(
        max_length=50
    )

    password = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.username

# this class is used for creating patient database, storing other details
class PatientDatabase(models.Model):

    CHOICE3=(
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others")
    )

    userInstance = models.OneToOneField(
        PatientRegister,
        on_delete=models.CASCADE
    )
    firstname = models.CharField(
        max_length=50,
        default=None,
        blank=True
    )

    lastname = models.CharField(
        max_length=50,
        default=None,
        blank=True
    )

    address = models.CharField(
        max_length=500,
        default=None,
        blank=True
    )

    emailID = models.EmailField(
        max_length=200,
        default=None,
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        default=None,
        blank=True
    )

    gender = models.CharField(
        max_length=50,
        choices=CHOICE3,
        blank=True
    )

    locationadd = models.CharField(
        max_length=500,
        default=None,
        blank=True
    )

    sickdetail = models.CharField(
        max_length=500,
        default=None,
        blank=True
    )

    def __str__(self):
        return self.userInstance.username


def create_profile(sender, instance, created, **kwargs):
    if created:
        PatientDatabase.objects.create(userInstance=instance)

post_save.connect(create_profile, sender=PatientRegister)

class ReceptionistRegister(models.Model):

    username = models.CharField(
        max_length=50
    )

    password = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.username

class ReceptionistDatabase(models.Model):

    CHOICE4 = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others")
    )

    userInstance = models.OneToOneField(
        ReceptionistRegister,
        on_delete=models.CASCADE
    )

    firstname = models.CharField(
        max_length=20,
        default=None
    )

    lastname = models.CharField(
        max_length=20,
        default=None
    )

    address = models.CharField(
        max_length=500,
        default=None
    )

    emailID = models.CharField(
        max_length=200,
        default=None
    )

    phone = models.CharField(
        max_length=10,
        default=None
    )

    gender = models.CharField(
        max_length=100,
        default=None,
        choices=CHOICE4
    )

    def __str__(self):
        return self.userInstance.username

class HRRegister(models.Model):

    username = models.CharField(
        max_length=50
    )

    password = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.username

class HRDatabase(models.Model):

    CHOICE5 = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others")
    )

    userInstance = models.OneToOneField(
        HRRegister,
        on_delete=models.CASCADE
    )

    firstname = models.CharField(
        max_length=20,
        default=None
    )

    lastname = models.CharField(
        max_length=20,
        default=None
    )

    address = models.CharField(
        max_length=500,
        default=None
    )

    emailID = models.CharField(
        max_length=200,
        default=None
    )

    phone = models.CharField(
        max_length=10,
        default=None
    )

    gender = models.CharField(
        max_length=100,
        default=None,
        choices=CHOICE5
    )

    def __str__(self):
        return self.userInstance.username

class Appointment(models.Model):

    user = models.CharField(
        max_length=50,
        default=None
    )

    Doctor = models.ForeignKey(
        DoctorDatabase,
        default=None,
        on_delete=models.CASCADE
    )

    Date = models.DateField(
        ("Date"),
        default=datetime.date.today
    )

    STATUS = (
        ("Pending", 'Pending'),
        ("Approved", 'Approved'),
        ("Rejected", 'rejected'),
    )

    status = models.CharField(
        max_length=2,
        choices=STATUS,
        default="Pending"
    )

    message = models.CharField(
        max_length=1000,
        default="Pending Approval"
    )

    def __str__(self):
        return str(self.user)