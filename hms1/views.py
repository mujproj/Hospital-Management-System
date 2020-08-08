from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

# this functioon is used to check if a string contaiins alphabet
def checkAlpha(s):

    return any(c.isalpha() for c in s)

# this function is used for displaying home page
def home(request):

    return render(request, 'home.html', {})

# this function is used for displaying contact page
def contact(request):

    return render(request, 'contact.html', {})

def about(request):

    return render(request, 'about.html', {})

def help(request):

    return render(request, 'help.html', {})

# this function is used for displaying the doctor portal
def displayDP(request):

    return render(request, 'doctor/doctorportal.html', {})
    
# this function is used for displaying doctor registration form
def displayDRF(request):

    doctorRegisterForm = DoctorRegistrationForm()
    return render(request, 'doctor/doctorregisterform.html', {'doctorRegisterForm': doctorRegisterForm})

# this function is used for making credentials work of the doctor registration form
def afterDRF(request):

    if request.method == "POST":

        doctorRegisterForm = DoctorRegistrationForm(request.POST)
        if doctorRegisterForm.is_valid():

            if request.POST["username"].isdigit():

                return render(request, 'doctor/doctorregisterform.html', {'doctorRegisterForm': doctorRegisterForm, 'error': "Username should not any numeric value"})

            # print(request.POST["username"])
            if len(request.POST["password"]) < 8:

                return render(request, 'doctor/doctorregisterform.html', {'doctorRegisterForm': doctorRegisterForm, 'error': "Password should be more than 8 characters"})

            if request.POST["password"] != request.POST["password_again"]:

                return render(request, 'doctor/doctorregisterform.html', {'doctorRegisterForm': doctorRegisterForm, 'error': "Passwords donot match"})

            user = DoctorRegister(username=doctorRegisterForm.cleaned_data['username'], password=doctorRegisterForm.cleaned_data['password'])
            user.save()
            return redirect('displayDLF')

        else:

            return render(request, 'doctor/doctorregisterform.html', {'doctorRegisterForm', doctorRegisterForm})

# this function is used for displaying the doctor login form
def displayDLF(request):

    doctorLoginForm = DoctorLoginForm()
    return render(request, 'doctor/doctorLoginForm.html', {'doctorLoginForm': doctorLoginForm})

# this function is used for after credentials of doctor login form
def afterDLF(request):

    if request.method == "POST":

        doctorLoginForm = DoctorLoginForm(request.POST)
        if doctorLoginForm.is_valid():

            username = request.POST['username']
            password = request.POST['password']

            data = DoctorRegister.objects.filter(username=username, password=password)
            if data:
                request.session['username'] = username
                global session
                session = request.session

                global keyvalue
                keyvalue = 0
                return redirect('doctorProfile')

            if username not in DoctorRegister.objects.values_list('username', flat=True):
                return render(request, 'doctor/doctorLoginForm.html', {'error': "Username Does Not Exists", 'doctorLoginForm': doctorLoginForm})

            if password not in DoctorRegister.objects.values_list('password', flat=True):
                return render(request, 'doctor/doctorLoginForm.html', {'error': "Password Does Not Exists", 'doctorLoginForm': doctorLoginForm})

            user = DoctorRegister.objects.filter().values('username', 'password')

            for u in user:
                if username in u['username']:
                    if password not in u['password']:
                        return render(request, 'doctor/doctorLoginForm.html', {'error': 'Username password mismatch', 'doctorLoginForm': doctorLoginForm})

                    else:
                        return redirect('doctorProfile')
            # print(username)
            return render(request, 'doctor/doctorLoginForm.html')

            # return redirect('displayDDF')
        else:

            return render(request, 'doctor/doctorLoginForm.html')

# this function is used for displaying doctor database form
def displayDDF(request):

    doctorDatabaseForm = DoctorDatabaseForm()
    return render(request, 'doctor/doctorDatabaseForm.html', {'doctorDatabaseForm': doctorDatabaseForm})

# this function is used for after credentials of doctor database form
def afterDDF(request):

    if request.method == "POST":
        # print("ERROR")
        doctorDatabaseForm = DoctorDatabaseForm(request.POST)
        print(doctorDatabaseForm.errors)
        print(doctorDatabaseForm.non_field_errors)
        if doctorDatabaseForm.is_valid():

            print("HI")
            if request.POST["firstname"].isdigit():

                # print("HI")
                return render(request, 'doctor/doctorDatabaseForm.html', {'doctorDatabaseForm': doctorDatabaseForm, 'error': 'First Name should not contain any numeric value'})

            if request.POST["lastname"].isdigit():

                # print("HI")
                return render(request, 'doctor/doctorDatabaseForm.html', {'doctorDatabaseForm': doctorDatabaseForm, 'error': 'Last Name Should Not contain any numeric value'})

            if  checkAlpha(request.POST["phone"]):

                # print("HI")
                return render(request, 'doctor/doctorDatabaseForm.html', {'doctorDatabaseForm': doctorDatabaseForm, 'error': 'Phone number should not contain any character'})

            user = DoctorRegister.objects.get(username=request.session["username"])
            print("//", user)
            DoctorDatabase.objects.filter(userInstance=user).update(firstname=doctorDatabaseForm.cleaned_data['firstname'], lastname=doctorDatabaseForm.cleaned_data['lastname'], speciality=doctorDatabaseForm.cleaned_data['speciality'], address=doctorDatabaseForm.cleaned_data['address'], emailID=doctorDatabaseForm.cleaned_data['emailID'], phone=doctorDatabaseForm.cleaned_data['phone'], gender=doctorDatabaseForm.cleaned_data['gender'])
            # print(a)
            return render(request, 'doctor/doctorDatabaseForm.html', {'doctorDatabaseForm': doctorDatabaseForm})

        else:

            print(" ithere", doctorDatabaseForm.errors)
            return render(request, 'doctor/doctorDatabaseForm.html', {'doctorDatabaseForm': doctorDatabaseForm})

# this function is used to display doctor profile
def doctorProfile(request):

    user = DoctorRegister.objects.get(username=request.session["username"])
    allobj = DoctorDatabase.objects.get(userInstance=user)
    return render(request, 'doctor/profile.html', {'allobj': allobj})

# this function is used to display new appoints
def newAppoints(request):

    user = DoctorRegister.objects.get(username=request.session["username"])
    # print(type(user))
    a = DoctorDatabase.objects.get(userInstance=user)
    c = ""
    # print(c)
    p = Appointment.objects.filter(Doctor=a).all()
    print(p)
    # user = Appointment.objects.filter()
    return render(request, 'doctor/newAppointments.html', {'allobj': p})

# this function is used to display prescriptions
def prescription(request):

    return render(request, 'doctor/prescription.html', {})

# this function is used to doctorloggout
def doctorLogout(request):

    del request.session['username']
    request.session.modified=True
    global keyvalue
    keyvalue=0
    return redirect('displayDLF')
    
# this function is used for displaying patient portal
def displayPP(request):

    return render(request, 'patient/patientportal.html', {})

# this function is used for displaying patient register form
def displayPRF(request):

    patientRegisterForm = PatientRegisterForm()
    return render(request, 'patient/patientregisterform.html', {'patientRegisterForm': patientRegisterForm})

# this function is used for credentials after patient register form
def afterPRF(request):

    if request.method == "POST":

        patientRegisterForm = PatientRegisterForm(request.POST)
        if patientRegisterForm.is_valid():

            # request.session["email"] = request.POST["emailID"]

            if request.POST["username"].isdigit():

                return render(request, 'patient/patientregisterform.html', {'patientRegisterForm': patientRegisterForm, 'error': 'Username should not contain any numeric value'})

            if len(request.POST["password"]) < 8:

                return render(request, 'patient/patientregisterform.html', {'patientRegisterForm': patientRegisterForm, 'error': 'Password should not be less than 8 characters'})

            if request.POST["password"] != request.POST["password_again"]:

                return render(request, 'patient/patientregisterform.html', {'patientRegisterForm': patientRegisterForm, 'error': 'Passwords donot match'})

            user = PatientRegister(username=patientRegisterForm.cleaned_data['username'], password=patientRegisterForm.cleaned_data['password'])
            user.save()
            return redirect('displayPLF')

        else:

            return render(request, 'patient/patientregisterform.html', {'patientRegisterForm': patientRegisterForm})

# this function is used for displaying patient login form
def displayPLF(request):

    patientLoginForm = PatientLoginForm()
    return render(request, 'patient/patientLoginForm.html', {'patientLoginForm': patientLoginForm})

# this function is used for after patient login credentials
def afterPLF(request):

    if request.method == "POST":

        patientLoginForm = PatientLoginForm(request.POST)
        if patientLoginForm.is_valid():
            
            username = request.POST['username']
            password = request.POST['password']

            data = PatientRegister.objects.filter(username=username, password=password)
            if data:
                request.session['username'] = username
                global session
                session = request.session

                global keyvalue
                keyvalue = 0
                return redirect('profile')

            if username not in PatientRegister.objects.values_list('username', flat=True):
                return render(request, 'patient/patientLoginForm.html', {'error': "Username Does Not Exists", 'patientLoginForm': patientLoginForm})

            if password not in PatientRegister.objects.values_list('password', flat=True):
                return render(request, 'patient/patientLoginForm.html', {'error': "Password Does Not Exists", 'patientLoginForm': patientLoginForm})

            user = PatientRegister.objects.filter().values('username', 'password')

            for u in user:
                if username in u['username']:
                    if password not in u['password']:
                        return render(request, 'patient/patientLoginForm.html', {'error': 'Username password mismatch', 'patientLoginForm': patientLoginForm})

                    else:
                        return redirect('profile')

            return render(request, 'patient/patientLoginForm.html')

            # return redirect('displayPDF')

        else:

            return render(request, 'patient/patientLoginForm.html', {'patientLoginForm': patientLoginForm})

# this function is used for displaying the patient database form
def displayPDF(request):

    patientDatabaseForm = PatientDatabaseForm()
    return render(request, 'patient/patientdatabaseform.html', {'patientDatabaseForm': patientDatabaseForm})

# this function is used for after credentials of the patient database form
def afterPDF(request):

    if request.method == "POST":

        patientDatabaseForm = PatientDatabaseForm(request.POST)
        if patientDatabaseForm.is_valid():
            
            if request.POST["firstname"].isdigit():

                return render(request, 'patient/patientdatabaseform.html', {'patientDatabaseForm': patientDatabaseForm, 'error': 'First Name should not contain any numeric value'})

            if request.POST["lastname"].isdigit():

                return render(request, 'patient/patientdatabaseform.html', {'patientDatabaseForm': patientDatabaseForm, 'error': 'Last Name Should Not contain any numeric value'})

            if  checkAlpha(request.POST["phone"]):

                return render(request, 'patient/patientdatabaseform.html', {'patientDatabaseForm': patientDatabaseForm, 'error': 'Phone number should not contain any character'})

            user = PatientRegister.objects.get(username=request.session["username"])
            PatientDatabase.objects.filter(userInstance=user).update(firstname=patientDatabaseForm.cleaned_data['firstname'], lastname=patientDatabaseForm.cleaned_data['lastname'], address=patientDatabaseForm.cleaned_data['address'], emailID=patientDatabaseForm.cleaned_data['emailID'], phone=patientDatabaseForm.cleaned_data['phone'], gender=patientDatabaseForm.cleaned_data['gender'], locationadd=patientDatabaseForm.cleaned_data['locationadd'], sickdetail=patientDatabaseForm.cleaned_data['sickdetail'])
            return render(request, 'patient/patientdatabaseform.html', {'patientDatabaseForm': patientDatabaseForm})

        else:

            return render(request, 'patient/patientdatabaseform.html', {'patientDatabaseForm': patientDatabaseForm})

# this function is used to display patient your appointments
def yourAppointments(request):

    b = []
    allobj = Appointment.objects.filter(user=request.session["username"])
    for i in allobj:
        b.append(i)
    # print(allobj.Date)
    return render(request, 'patient/apointment.html', {'allobj': b})

# this function is used to display your patient payment history
def yourPaymentHistory(request):

    return render(request, 'patient/invoicepayment.html', {})

# this function is used to display patient profile
def patientProfile(request):

    user = PatientRegister.objects.get(username=request.session["username"])
    allobj = PatientDatabase.objects.get(userInstance=user)
    return render(request, 'patient/profile.html', {'allobj': allobj})

# this function is used to display patient medical history
def patientMedicalHistory(request):

    return render(request, 'patient/medicalhistory.html', {})

# this function is used to display the payment form
def displayPaymentForm(request):

    return render(request, 'patient/paymentForm.html')

# this function is used for patient logout
def patientLogout(request):

    del request.session['username']
    request.session.modified=True
    global keyvalue
    keyvalue=0
    return redirect('displayPLF')

# this function is used for new appointment form
def displayNAF(request):

    newAppointmentForm = AppointmentForm()
    return render(request, 'patient/newAppointmentForm.html', {'newAppointmentForm': newAppointmentForm})

# this function is used for after new appointment form
def afterNAF(request):

    if request.method == "POST":

        newAppointmentForm = AppointmentForm(request.POST)
        if newAppointmentForm.is_valid():
            # u = PatientRegister(username=request.session["username"])
            # print(user)
            fix = Appointment(user=newAppointmentForm.cleaned_data["user"], Doctor=newAppointmentForm.cleaned_data['Doctor'], Date=newAppointmentForm.cleaned_data['Date'])
            fix.save()
            return render(request, 'patient/newAppointmentForm.html', {'newAppointmentForm': newAppointmentForm, 'message': 'the appointment has been fixed'})

        else:

            return render(request, 'patient/newAppointmentForm.html', {'newAppointmentForm': newAppointmentForm})

# this fucntion is used to display the receptionist portal
def displayRP(request):

    allobj = Appointment.objects.all()
    print(allobj)
    return render(request, 'receptionist/receptionistportal.html', {'allobj': allobj})

    # return render(request, 'receptionist/receptionistportal.html', {})

# this function is used to display the receptionist login form
def displayRLF(request):

    receptionistLoginForm = ReceptionistLoginForm()
    return render(request, 'receptionist/receptionistLoginForm.html', {'receptionistLoginForm': receptionistLoginForm})

# this function is used for after cred of receptionist login form
def afterRLF(request):

    if request.method == "POST":

        receptionistLoginForm = ReceptionistLoginForm(request.POST)
        if receptionistLoginForm.is_valid():

            username = request.POST['username']
            password = request.POST['password']

            data = ReceptionistRegister.objects.filter(username=username, password=password)
            if data:
                request.session['username'] = username
                global session
                session = request.session

                global keyvalue
                keyvalue = 0
                return redirect('displayRP')

            if username not in ReceptionistRegister.objects.values_list('username', flat=True):
                return render(request, 'receptionist/receptionistLoginForm.html', {'error': "Username Does Not Exists", 'receptionistLoginForm': receptionistLoginForm})

            if password not in ReceptionistRegister.objects.values_list('password', flat=True):
                return render(request, 'receptionist/receptionistLoginForm.html', {'error': "Password Does Not Exists", 'receptionistLoginForm': receptionistLoginForm})

            user = ReceptionistRegister.objects.filter().values('username', 'password')

            for u in user:
                if username in u['username']:
                    if password not in u['password']:
                        return render(request, 'receptionist/receptionistLoginForm.html', {'error': 'Username password mismatch', 'receptionistLoginForm': receptionistLoginForm})

                    else:
                        return redirect('displayRP')

            return render(request, 'receptionist/receptionistLoginForm.html')

            # return redirect('displayPDF')

        else:

            return render(request, 'receptionist/receptionistLoginForm.html', {'receptionistLoginForm': receptionistLoginForm})

# this is to display all the appoitments
def allappointments(request):
    pass
# this function is used for receptionist logout
def receptionistLogout(request):

    del request.session['username']
    request.session.modified=True
    global keyvalue
    keyvalue=0
    return redirect('displayRLF')

# this function is used for displaying hr portal
def displayHRP(request):
    
    do = DoctorDatabase.objects.all()
    return render(request, 'hr/hrportal.html', {'allobj': do})

# this function is used for displaying hr login form
def displayHRLF(request):

    hrLoginForm = HRLoginForm()
    return render(request, 'hr/hrLoginForm.html', {'hrLoginForm': hrLoginForm})

# this function is used for after cred of hr login form
def afterHRLF(request):

    if request.method == "POST":

        hrLoginForm = HRLoginForm(request.POST)
        if hrLoginForm.is_valid():

            username = request.POST['username']
            password = request.POST['password']

            data = HRRegister.objects.filter(username=username, password=password)
            if data:
                request.session['username'] = username
                global session
                session = request.session

                global keyvalue
                keyvalue = 0
                return redirect('displayHRP')

            if username not in HRRegister.objects.values_list('username', flat=True):
                return render(request, 'hr/hrLoginForm.html', {'error': "Username Does Not Exists", 'hrLoginForm': hrLoginForm})

            if password not in HRRegister.objects.values_list('password', flat=True):
                return render(request, 'hr/hrLoginForm.html', {'error': "Password Does Not Exists", 'hrLoginForm': hrLoginForm})

            user = HRRegister.objects.filter().values('username', 'password')

            for u in user:
                if username in u['username']:
                    if password not in u['password']:
                        return render(request, 'hr/hrLoginForm.html', {'error': 'Username password mismatch', 'hrLoginForm': hrLoginForm})

                    else:
                        return redirect('displayHRP')

            return render(request, 'hrist/hrLoginForm.html')

            # return redirect('displayPDF')

        else:

            return render(request, 'hr/hrLoginForm.html', {'hrLoginForm': hrLoginForm})

# this function is used to display the doctors
def payments(request):

    return render(request, 'hr/payments.html')

# this function is used to logout
def hrLogout(request):

    del request.session['username']
    request.session.modified=True
    global keyvalue
    keyvalue=0
    return redirect('displayHRLF')
