
#_______________________ POST APP'in views'i _____________________

from django.shortcuts import render



def post_index(request):
    return render(request, "post/index.html", context = {})




def post_detail(request):
    return render(request, "post/detail.html", context = {})



def post_create(request):
    return render(request, "post/create.html", context = {})


def post_update(request):
    return render(request, "post/update.html", context = {})


def post_delete(request):
    return render(request, "post/delete.html", context = {})