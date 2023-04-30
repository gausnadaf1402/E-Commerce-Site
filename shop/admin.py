from django.contrib import admin
from .models import Product,Order

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(category='default')
    list_display=['id','title','price','discount_price','category','description','image']
    search_fields=('title',)
    actions=('change_category_to_default',)
    list_editable=('price',)
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','items','name','email','address','city','state','zip','total']

