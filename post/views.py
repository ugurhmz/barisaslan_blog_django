
#_______________________ POST APP'in views'i _____________________

from django.shortcuts import render, get_object_or_404, redirect, Http404
from .models import Post
from .forms import PostForm, CommentForm
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.utils.text import  slugify



def post_index(request):
    posts = Post.objects.all()
    return render(request,"post/index.html", {'posts' : posts})



def post_detail(request,slug):
    post = get_object_or_404(Post, slug=slug)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url()) #Postun ilgili detay sayfası : post.get_absolute_url()

    context = {
        'post':post,
        'form':form,
    }


    return render(request, "post/detail.html", context=context)




def post_create(request):
    if not request.user.is_authenticated:
        return Http404()


    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user #istek yapan kullanıcıyı getiriyoruz,request.user ile.
        post.save()
        messages.success(request,"Başarılı bir şekilde oluşturuldu...")
        return  HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form' : form,
    }

    return render(request, "post/form.html", context= context)






def post_update(request ,slug ):
    if not request.user.is_authenticated:
        return Http404()



    post = get_object_or_404(Post,slug = slug)
    form = PostForm(request.POST or None , request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request,"Güncelleme başarılı....", extra_tags="myMessageCSS")
        return HttpResponseRedirect(post.get_absolute_url())

    context =  {
        'form' : form
    }

    return render(request,"post/form.html", context= context)





def post_delete(request,slug):
        if not request.user.is_authenticated:
            return Http404()

        obj = get_object_or_404(Post,slug=slug)
        obj.delete()
        messages.info(request,"Silindi..")

        return redirect('post_index')
