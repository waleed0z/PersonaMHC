from django.shortcuts import render, redirect
from .models import Post

def create_post(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        body = request.POST['body']
        post = Post(name=name, subject=subject, body=body)
        post.save()
        return redirect('read_posts')
    else:
        return render(request, 'create_post.html')

def read_posts(request):
    posts = Post.objects.all()
    return render(request, 'read_posts.html', {'posts': posts})


