from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user= authenticate(username=username, password=password)

        login(request,user)
        return redirect('home')

    context = {
        'form':form,
        'title' :'Giriş Yap'
    }

    return render(request,"accounts/form.html", context=context)


def register_view(request):
    form =RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.is_staff = True #Admin paneline girmesi için..
        user.save()
        new_user = authenticate(username = user.username, password=password) #yeni kullanıcı oluşturuyoruz
        login(request,new_user) #login yapıyoruz
        return redirect('home') #ardından anasayfaya yönlendiriyoruz..

    return render(request, "accounts/form.html", {'form':form, 'title':'Üye Ol'})



def logout_view(request):
    logout(request)
    return redirect('home')