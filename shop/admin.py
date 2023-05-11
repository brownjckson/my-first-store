from django.contrib import admin
from .models import Banner, Category, Marca, Color, Size, Product, ProductAttribute

# Register your models here.
admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(Marca)
admin.site.register(Color)
admin.site.register(Size)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','marca','color','size','status')
    list_editable = ('status',)
admin.site.register(Product,ProductAdmin)

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id','product','price','color','size')

admin.site.register(ProductAttribute,ProductAttributeAdmin)
