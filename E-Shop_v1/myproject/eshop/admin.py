from django.contrib import admin
from . models import Item,Order,OrderItem
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','image','price','description','fabric_origin','made_in','color','size','pub_date')
    list_display_links = ['title','image']
    list_editable = ['price','color','size',]
    list_filter = ['title','made_in','size','pub_date',]
    prepopulated_fields = {'slug': ('title',)}

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered', ]
    list_filter = ['ordered', ]

admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
