from django.urls import path
from wishlist import views

app_name = 'wishlist'

urlpatterns = [

    path('add/<product_id>', views.wishlist_add, name='wishlist_add'),
    path('remove/<product_id>', views.wishlist_remove, name='wishlist_remove'),
    path('', views.wishlist_detail, name='wishlist_detail')

]
