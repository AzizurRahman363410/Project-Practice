from django.db.models import Q
from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator
from .models import Post
from django.contrib import messages
from .forms import PostForm
# Create your views here.
def home(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 6)  # Show 25 contacts per page

    page = request.GET.get('page')
    post = paginator.get_page(page)
    context = {
        'post_list': post
    }

    return render(request,'blog/home.html',context)

def detail(request,pk):
    context = {
        'post_detail':get_object_or_404(Post,pk=pk)
    }
    return render(request, 'blog/detail.html', context)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)  #Optional   just do ----> form.save()
            instance.save()
            messages.success(request, 'Your Post are successfully created ')
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})
# different way you can do it
    # form = PostForm(request.POST or None, request.FILES or None)
    # if form.is_valid():
    #     form.save()
    #     return redirect('home')
    #
    # return render(request, 'blog/post_form.html', { 'form': form})
def update_post(request,pk):
    instance = get_object_or_404(Post,pk=pk)
    form = PostForm(request.POST or None, request.FILES or None,instance=instance)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/post_form.html', { 'form': form})
def delete_post(request,pk):
    instance = get_object_or_404(Post,pk=pk)
    instance.delete()
    messages.success(request,'Your Post are successfully deleted ')
    return redirect('home')
def search(request):
    if request.method == 'POST':
        query = request.POST.get('q')
        post_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    return render(request, 'blog/search.html', {'post_list': post_list, 'query': query})