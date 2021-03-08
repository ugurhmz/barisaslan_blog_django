
#_______________________ POST APP'in views'i _____________________

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.contrib import messages

def post_index(request):
    posts = Post.objects.all()

    return render(request,"post/index.html", {'posts' : posts})



def post_detail(request,detail_id ):
    post = get_object_or_404(Post, id=detail_id)
    return render(request, "post/detail.html", {'post':post})




def post_create(request):

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save()
        messages.success(request,"Başarılı bir şekilde oluşturuldu...")
        return  HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form' : form,
    }

    return render(request, "post/form.html", context= context)






def post_update(request ,detail_id ):
    post = get_object_or_404(Post,id = detail_id)
    form = PostForm(request.POST or None , request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request,"Güncelleme başarılı....", extra_tags="myMessageCSS")
        return HttpResponseRedirect(post.get_absolute_url())

    context =  {
        'form' : form
    }

    return render(request,"post/form.html", context= context)








def post_delete(request,detail_id):
        obj = get_object_or_404(Post,id=detail_id)
        obj.delete()
        messages.info(request,"Silindi..")

        return redirect('post_index')
