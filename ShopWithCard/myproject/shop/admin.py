from django.contrib import admin
from .models import Product,Contact,Orders,OrderUpdate
# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['product_id','product_name','product_price','image','description','pub_date']
admin.site.register(Product,ProductModelAdmin)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
