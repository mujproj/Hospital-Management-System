from django import forms
from .models import *

class DoctorRegistrationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(DoctorRegistrationForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "User Name"
        self.fields["password"].label = "Password"
        self.fields["password_again"].label = "Confirm Your Password"

    class Meta:

        model = DoctorRegister
        fields = '__all__'

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter a username'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter The Password'
            }
        )
    )

    password_again = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Please Confirm Your Password'
            }
        )
    )

# doctor login form
class DoctorLoginForm(forms.Form):

    def __init__(self, *args, **kwargs):

        super(DoctorLoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "User Name"
        self.fields["password"].label = "Password"

    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your username'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Please Enter Your Password'
            }
        )
    )

class DoctorDatabaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(DoctorDatabaseForm, self).__init__(*args, **kwargs)
        self.fields['firstname'].label = 'First Name'
        self.fields['lastname'].label = 'Last Name'
        self.fields['emailID'].label = 'Email Address'
        self.fields['phone'].label = 'Contact Number'

    class Meta:

        model = DoctorDatabase
        fields = ['firstname', 'lastname', 'speciality', 'address', 'emailID', 'phone', 'gender']

class PatientRegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(PatientRegisterForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "User Name"
        self.fields["password"].label = "Password"
        self.fields["password_again"].values = "Confirm Your Password"

    class Meta:

        model = PatientRegister
        fields = '__all__'

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter a username'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter the password'
            }
        )
    )        

    password_again = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Please Confirm Your Password'
            }
        )
    )

# patient Login Form
class PatientLoginForm(forms.Form):

    def __init__(self, *args, **kwargs):

        super(PatientLoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "User Name"
        self.fields["password"].label = "Password"        

    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your Username'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Please Enter Your Password'
            }
        )
    )

class PatientDatabaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(PatientDatabaseForm, self).__init__(*args, **kwargs)
        self.fields['firstname'].label = 'First Name'
        self.fields['lastname'].label = 'Last Name'
        self.fields['emailID'].label = 'Email Address'
        self.fields['phone'].label = 'Contact Number'

    class Meta:

        model = PatientDatabase
        fields = ['firstname', 'lastname', 'address', 'emailID', 'phone', 'gender', 'locationadd', 'sickdetail']

class ReceptionistLoginForm(forms.Form):
    
    def __init__(self, *args, **kwargs):

        super(ReceptionistLoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "User Name"
        self.fields["password"].label = "Password"

    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your Username'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Please Enter Your Password'
            }
        )
    )

class HRLoginForm(forms.Form):
    
    def __init__(self, *args, **kwargs):

        super(HRLoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "User Name"
        self.fields["password"].label = "Password"

    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your Username'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Please Enter Your Password'
            }
        )
    )

class AppointmentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields["Doctor"].label = "Please Select Doctor"
        self.fields["Date"].label = "Please Select a Date"

    class Meta:

        model = Appointment
        fields = ['user', 'Doctor', 'Date']
