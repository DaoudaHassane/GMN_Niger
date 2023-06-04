from django.contrib import admin
from .models import Category, Item, order, cart
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = [
        'title',
        'price',
        'discount_price',
        'created_at',
        'img'
    ]

#class CategoryAdmin(admin.ModelAdmin):
    #prepopulated_fields = {'slug': ('title',)}
    #list_display = [
        #'title',
        #'slug'
        #]"""
admin.site.register(Item, ItemAdmin)
admin.site.register(order)
admin.site.register(cart)
admin.site.register(Category)#, CategoryAdmin)