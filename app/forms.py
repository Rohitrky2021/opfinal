# class form control is of bootstrap
from django import forms 
from django.contrib.auth.forms import *
        
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from .models import *

class MyPasswordChangeForm(PasswordChangeForm):
 old_password =forms.CharField(label=_('old Password'),widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))
 new_password1 =forms.CharField(label=_('New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html)# class CustomerRegistrationForm(UserCreationform):
 new_password2 =forms.CharField(label=('Confirm New Password (again)'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
  
class Meta:
    model=User
    fields=['username','email','password1','password2']
    labels={'username':'Username','email':'Email','password1':'Password','password2':'Confirm Password (again)'}
    widgets={'username':forms.TextInput(attrs={'class':'form-control'})}

# login forms do not require data to store so
# models are not required here
 
class LoginForm(AuthenticationForm):
  username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,
  'class':'form-control'}))
  password= forms.CharField(label=_("Password"), strip=False,
  widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
  'class':'form-control'}))

class CustomerRegistrationForms(UserCreationForm):
  username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
  email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'})) 
  password1 =forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))# class CustomerRegistrationForm(UserCreationform):
  password2 =forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
class MyPasswordResetForm(PasswordResetForm):
  email=forms.EmailField(label=_('Email'),max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
  
  new_password1 =forms.CharField(label=_('New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html)# class CustomerRegistrationForm(UserCreationform):
  new_password2 =forms.CharField(label=('Confirm New Password (again)'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
  
class CustomerProfileForm(forms.ModelForm):
  class Meta:
    model=Customer
    fields=['name','locality','city','state','zipcode']
    widgets={'name':forms.TimeInput(attrs={'class':'form-control'}),'locality':forms.TextInput(attrs={'class':'form-control'})
    ,'city':forms.TimeInput(attrs={'class':'form-control'}),
    'state':forms.Select(attrs={'class':'form-control'})
    ,'zipcode':forms.NumberInput(attrs={'class':'form-control'})}  

