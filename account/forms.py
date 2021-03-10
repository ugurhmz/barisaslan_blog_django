
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User# Djangonun User modelini import ettik



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Kullanıcı Adı")
    password = forms.CharField(max_length=100, label="Parola", widget=forms.PasswordInput)


    def clean(self):  #form kontrolü yapmak için
        username = self.cleaned_data.get('username') #cleaned_data girişi onaylarsa değişkenlere veri aktaracak.
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Kullanıcı adını veya parolayı yanlış girdiniz!")
        return super(LoginForm, self).clean()

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label="Kullanıcı Adı")
    password1 = forms.CharField(max_length=100, label="Parola", widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label="Parola Doğrula", widget=forms.PasswordInput)

    class Meta: #bu formun hangi modeli referans olcağını belirtiyoruz
            model = User
            fields = [
                'username',
                'password1',
                'password2'

            ]


    def clean_password2(self): #bu alanının kontrolü için
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')


        if (password1 and password2) and password1!=password2:
            #eğer her iki alanda doldurulmuşsa ve birbirine denk değilse..
            raise forms.ValidationError("Parolalar uyuşmuyor!")
        return password2



