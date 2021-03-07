from django.shortcuts import render




def home_view(request):
        if request.user.is_authenticated:
            context = {
                'isim' :'Uğur Giriş Yapmış',
            }
        else:
            context = {
                'isim' : 'Misafir Girişi',
            }


        return render(request, "home.html", context = context)