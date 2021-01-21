from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blog(request, *args, **kwargs):
    blog_count = len(Blog.objects.all())
    blogs = Blog.objects.order_by('-date')[:5]
    for blog in blogs:
        blog.date = blog.date.strftime("%B %d, %Y")
    return render(request, 'blog/blog.html',{'blogs': blogs, 'blog_num': blog_count})


def details(request, blog_id):
    blog = get_object_or_404(Blog,pk = blog_id )
    return render(request, 'blog/details.html', {'blog':blog})
