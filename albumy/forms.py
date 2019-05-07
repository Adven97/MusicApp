from django import forms
from django.contrib.auth import authenticate, get_user_model
from .models import Album, UserData
class RegisterForm(forms.Form):

    name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    nick = forms.CharField(max_length=40)
    email = forms.CharField(max_length=60)
    password = forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
    nick = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self, *args, **kwargs):
        nick = self.cleaned_data.get('nick')
        password = self.cleaned_data.get('password')
        if nick and password:
            user = checkIfExist(nick)
            passw = checkIfExist(password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not passw:
                raise forms.ValidationError('Incorrect Password')
        return super(LoginForm, self).clean(*args, **kwargs)

    
def checkIfExist(nik):
        for x in UserData.objects.all():
            if x.nick == nik:
                return True
        return False
