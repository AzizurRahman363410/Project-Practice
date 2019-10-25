from django.shortcuts import render,get_object_or_404,redirect,redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib import messages
from .models import Post
# Create your views here.
def home(request):
    return render(request, 'home.html')

class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('signup')

    # def get_success_url(self):
    #     messages.success(self.request, 'Profile updated')
    #     return reverse_lazy('signup')

    # def get_success_url(self):
    #     messages.success(self.request, 'Profile updated')
    #     return reverse('signup')



def create_post(request):
    posts = Post.objects.all()
    response_data = {}

    if request.is_ajax():
        title = request.POST.get('title')
        description = request.POST.get('description')
        print('title is :',title)

        if title and description:
            response_data['title'] = title
            response_data['description'] = description

            Post.objects.create(
                title = title,
                description = description,
                )  


            return JsonResponse(response_data)

    return render(request, 'create_post.html', {'posts':posts})    


def delete_post(request, pk):
    posts = get_object_or_404(Post,pk=pk)
    posts.delete()
    return redirect('create_post')    
    
