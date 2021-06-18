from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('search', views.product_search, name='product_search'),
    path('<category_slug>', views.product_list, name='product_list_by_category'),
    path('<id>/<slug>', views.product_detail, name='product_detail'),
]
