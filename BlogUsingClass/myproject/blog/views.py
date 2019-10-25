from django.db.models import Q
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView,View
# Create your views here.



class BlogListView(ListView):
    model = Post
    context_object_name = 'post_list'
class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post_detail'

class BlogCreateView(CreateView):
    model = Post
    fields = ['title','image','content']
    success_url = '/'
class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'image', 'content']
    success_url = '/'
class BlogDeleteView(DeleteView):
    model = Post
    context_object_name = 'item'
    success_url = '/'
class BlogSearchView(ListView):
    model = Post
    def post(self, request, *args, **kwargs):
        query = request.POST.get('q')
        post_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        return render(request, 'blog/search_results.html', {'post_list': post_list, 'query': query})



    # using GET method
    # def get_queryset(self):  # new
    #     query = self.request.GET.get('q')
    #     post_list = Post.objects.filter(
    #         Q(title__icontains=query) | Q(content__icontains=query)
    #     )
    #     return post_list
    # template_name = 'search_results.html'







