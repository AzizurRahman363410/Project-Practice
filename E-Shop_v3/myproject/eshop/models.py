from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth.models import User
# Create your models here.
SIZE_CHOICE ={
    ('m','M'),
    ('l','L'),
    ('xl','XL'),
    ('fs','FS'),
    ('s','S'),
}

class Item(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='picture/')
    price = models.FloatField(blank=True, null=True , default='200')
    discount_price = models.FloatField(blank=True, null=True)
    description = models.TextField()
    fabric_origin = models.CharField(max_length=100)
    made_in = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=100, choices=SIZE_CHOICE,default='m')
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

  
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={"slug": self.slug})
    def get_remove_form_cart_url(self):
        return reverse("remove-form-cart", kwargs={"slug": self.slug})



class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()
    

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    def __str__(self):
        return self.phone
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'