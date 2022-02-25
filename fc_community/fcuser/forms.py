from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    useremail = forms.CharField(error_messages={'required': 'Please enter your email address'}, max_length=32, label="Enter email address")
    password = forms.CharField(error_messages={'required': 'Please enter your password'}, widget=forms.PasswordInput, label="Enter password")

    def clean(self):
        cleaned_data = super().clean()
        useremail = cleaned_data.get('useremail')
        password = cleaned_data.get('password')

        if useremail and password:
            try:
                fcuser = Fcuser.objects.get(useremail=useremail)
            except Fcuser.DoesNotExist:
                self.add_error('useremail', 'There is no email address registered')
                return
                
            if not check_password(password, fcuser.password):
                self.add_error('password', 'Incorrect password')
            else:
                self.user_id = fcuser.id