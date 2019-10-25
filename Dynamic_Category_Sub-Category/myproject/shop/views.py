from django.shortcuts import render
from .models import Category,Sub_Category,Product
# Create your views here.
def home(request):
    category_list = Category.objects.all();
    sub_category_list = Sub_Category.objects.all();
    context = {
        'category_list': category_list,
        'sub_category_list' : sub_category_list,
    }

    return render(request,'shop/home.html',context)