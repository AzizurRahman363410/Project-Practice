from django.contrib import admin
from .models import Category,Sub_Category,Product
# Register your models here.
class ProductAdminView(admin.ModelAdmin):
    list_display = ('id','title','image','description','pub_date',)

admin.site.register(Product, ProductAdminView)

class CategoryAdminView(admin.ModelAdmin):
    list_display = ('id','category_name','slug')
    prepopulated_fields = {'slug':('category_name',)}

admin.site.register(Category, CategoryAdminView)


class Sub_CategoryAdminView(admin.ModelAdmin):
   
    list_display = ('id','get_category_id','get_name_category','Sub_category_name','slug')
    prepopulated_fields = {'slug':('Sub_category_name',)}
    def get_name_category(self, obj):
        return obj.category.category_name
    get_name_category.short_description = 'category'
    def get_category_id(self, obj):
        return obj.category.id
    get_name_category.short_description = 'Id'

admin.site.register(Sub_Category, Sub_CategoryAdminView)