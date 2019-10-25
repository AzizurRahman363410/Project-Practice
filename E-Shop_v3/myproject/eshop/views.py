from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView,DetailView,View
from . models import Item,OrderItem,Order,Profile
from django.utils import timezone
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from . forms import SizeForm
from django.contrib.auth import login, logout
from django.contrib import auth
# Create your views here.
def home(request):
    all_prods = Item.objects.all()
    all_featured_Item = Item.objects.filter(price__gte='200')

    context = {
        'all_prods': all_prods,
        'all_featured_Item': all_featured_Item,
    }
    return render(request, 'eshop/index.html',context);

def contact(request):
    return render(request, 'eshop/contact.html');
def about(request):
    return render(request, 'eshop/about.html');

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone = request.POST['phone']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('this username already exists, Please Try another one')
            elif User.objects.filter(email=email).exists():
                 print('this email already taken , Please Try another one')
            else:
                user = User.objects.create(username= username, first_name=first_name, last_name=last_name, email=email,)
                user.set_password(password1)
                user.save()
                profile = Profile.objects.create(user=user, phone=phone)
                profile.save()
                return redirect('home')
        else:
            print('password are not equal')
            return render(request, 'eshop/register.html');
    else:
        return render(request, 'eshop/register.html');


def login(request):
    logout(request)
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        try:
            check_user = User.objects.get(email=email)
            print('user checking :', check_user)
            if check_user.check_password(password):
                print('Wow success')
                auth.login(request, check_user)
                return redirect('home')
            else:
                print('Does not success')
                return redirect('login')
        except ObjectDoesNotExist:
            return redirect('login')

    return render(request, 'eshop/account.html');

def checkout(request):
    return render(request, 'eshop/checkout.html');





def productList(request):










    return render(request, 'eshop/products.html');













    
def single_item(request,slug):
    if request.method == 'POST':
        form = SizeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SizeForm()
    context = {
        'all_prods': Item.objects.all(),
        'item': get_object_or_404(Item, slug=slug),
        'form': form

    }

    return render(request, 'eshop/single_item.html',context);
 

# cart begin

def add_to_cart(request,slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered = False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("order-summary")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart OldCart.")
            return redirect('home')

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date
        )
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart NewCart.")
    return redirect('product')




def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
            return redirect('product')
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("home")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("home")

class OrderSummaryView(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'eshop/order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")

def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("home")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("home")