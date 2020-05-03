from django import forms
from .models import *
from django.core.validators import validate_email

class Registerform(forms.ModelForm):

    class Meta:
        model = Register
        fields= '__all__'
        labels= {}
    def __init__(self,*args,**kwargs):
        super(Registerform,self).__init__(*args,**kwargs)
        self.fields['location'].empty_lable='select'
        self.fields['date_of_birth'].required = False
    def clean_username(self):
        user=self.cleaned_data['user_name']
        try:
            match = Register.objects.get(user_name= user)
        except:
            return self.cleaned_data['user_name']
        raise forms.ValidationError('username is taken')
    def clean_email(self):
        email=self.cleaned_data['email_id']
        try:
            mtch=validate_email(email)
        except:
            return forms.ValidationError("Email is not in correct format")
    def clean_confirm_passwowrd(self):
        pswrd = self.cleaned_data['password']
        cpswrd = self.cleaned_data['confirm_password']

        if pswrd != cpswrd:
            raise forms.ValidationError('your password did not match')
        else:
            if len(pswrd) < 8:
                raise forms.ValidationError("minimum 8 character are required")
            if pswrd.isdigit():
                raise forms.ValidationError("password should not contain all digits")





