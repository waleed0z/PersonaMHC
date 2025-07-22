from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def create_post(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        body = request.POST['body']
        attachment = request.FILES.get('attachment', None)
        post = Post(name=name, subject=subject, body=body, attachment=attachment)
        post.save()
        return redirect('read_posts')
    else:
        return render(request, 'create_post.html')

def read_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    # Calculate reading time for each post (200 words per minute)
    for post in posts:
        word_count = len(post.body.split())
        post.reading_time = max(1, round(word_count / 200))
    return render(request, 'read_posts.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # Calculate reading time (200 words per minute)
    word_count = len(post.body.split())
    reading_time = max(1, round(word_count / 200))
    return render(request, 'post_detail.html', {'post': post, 'reading_time': reading_time})

def my_static_page(request):
    return render(request, 'index.html')