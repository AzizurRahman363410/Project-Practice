from django.shortcuts import render, get_object_or_404
from .models import Category,Sub_Category,Product
from django.db.models import Q
# Create your views here.
def home(request,sub_category_slug=None):

    category_list = Category.objects.all();
    sub_category_list = Sub_Category.objects.all();
    products = Product.objects.all()
  
    if sub_category_slug:
        # sub_category = Sub_Category.objects.filter(slug=sub_category_slug)
        # cat = Sub_Category.objects.filter(sub_category.category=sub_category.category)
        # print('sub_category:    ',sub_category)
        # print('category:    ',cat)

        # # sub_category1 = Sub_Category.objects.filter(slug=sub_category_slug)
        # # print("product categories : ",sub_category1.category)
        # # if len(sub_category1)> 1:
        # #     print("categories length is more than one")
        # #     products = Product.objects.filter(category=sub_category.category)
        # # else:
        # #     print("categories length is less than one")
        sub_category =get_object_or_404(Sub_Category,slug=sub_category_slug)   
        products = Product.objects.filter(
            Q(sub_category=sub_category)&
            Q(category=sub_category.category)
        )
    context = {
        'category_list': category_list,
        'sub_category_list' : sub_category_list,
        'products':products,

    }

    return render(request,'shop/home.html',context)