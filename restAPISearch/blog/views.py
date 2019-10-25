from django.shortcuts import render
from api.models import Post
from .forms import PostCreateForm
# Create your views here.
def home(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostCreateForm(request.POST or None)
        if form.is_valid():
            Post.objects.create(
                title = form.cleaned_data['title'],
                description = form.cleaned_data['description']
            )
    else:
        form = PostCreateForm()
    context = {
        'posts':posts,
        'form':form
    }
    return render(request, 'blog\home.html',context)
