from django.urls import path
from .views import home, details, search, add_to_cart, cart, delete_cart


urlpatterns = [
    path('', home, name='index'),
    path('<id>/<str:slug>/', details, name='details'),
    path('cart/', cart, name="cart"),
    path('cart/delete', delete_cart, name="delete-cart"),
    path('product/<str:slug>/add-to-cart/', add_to_cart, name='add-to-cart'),
    path('search/', search, name='search'),
]
