from django.shortcuts import render
from .models import BlogPost,Category
# Create your views here.
def index(request):
    blog_post = BlogPost.objects.all()

    if 'category' in request.GET:
        # for finding category
        blog_post = blog_post.filter(category=int(request.GET.get('category')))


    context = {
        'posts':blog_post.order_by('-date_timeField')

    }
    return render(request,"index.html",context)

def post_view(request,pk):
    blog_post = BlogPost.objects.get(pk=pk)

    return render(request,"post.html", {'post':blog_post})