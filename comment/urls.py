from django.urls import path
from . import views

app_name='comment'

urlpatterns = [
    path('add/<product_id>/<order_id>', views.comment_save, name='comment_save'),

]