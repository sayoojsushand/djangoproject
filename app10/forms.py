from django import forms
from . models import SignUp

class SignUpForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput, max_length=8)
    ConfirmPassword = forms.CharField(widget=forms.PasswordInput, max_length=8)
    class Meta():
        model = SignUp
        fields = '__all__'

class LoginForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput, max_length=8)
    class Meta():
        model = SignUp
        fields = ('Email', 'Password')
    
class UpdateForm(forms.ModelForm):
    class Meta():
        model = SignUp
        fields = ('Name', 'Email', 'Age', 'Photo')
