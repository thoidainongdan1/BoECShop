from django.urls import path
from . import views

app_name='orders'

urlpatterns = [
    path('create', views.order_create, name='order_create'),
    path('process', views.order_save, name='order_save'),
    path('order_change_state/<order_id>', views.order_change_state, name='order_change_state'),
    path('admin/check_order', views.check_order, name='check_order'),
    path('remove/<order_id>', views.order_remove, name='order_remove'),
    path('comment/<order_id>', views.order_comment, name='order_comment'),
    path('detail/<order_id>', views.order_detail, name='order_detail'),
    path('', views.order_list, name='order_list'),  
]
