from django.urls import path
from . import views

app_name='cart'
urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<product_id>', views.cart_add, name='cart_add'),
    path('add_quantity/<product_id>', views.cart_add_quantity, name='cart_add_quantity'),
    path('remove/<product_id>', views.cart_remove, name='cart_remove'),

]