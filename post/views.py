
#_______________________ POST APP'in views'i _____________________

from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm


def post_index(request):
    posts = Post.objects.all()

    return render(request,"post/index.html", {'posts' : posts})




def post_detail(request,detail_id ):
    post = get_object_or_404(Post, id=detail_id)
    return render(request, "post/detail.html", {'post':post})






def post_create(request):
    form =PostForm()
    context = {
        'form' : form
    }

    return render(request, "post/form.html", context = context)


def post_update(request):
    return render(request, "post/update.html", context = {})


def post_delete(request):
    return render(request, "post/delete.html", context = {})