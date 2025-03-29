# urls.py
from django.urls import path
from .views import item_listapi, item_detail, item_list, item_create, item_update, item_delete
app_name = 'testapi'

urlpatterns = [
    path('', item_list, name='item_list'),
    path('new/', item_create, name='item_create'),
    path('<int:pk>/edit/', item_update, name='item_update'),
    path('<int:pk>/delete/', item_delete, name='item_delete'),
    path('api/items/', item_listapi, name='item_listapi'),
    path('api/items/<int:pk>/', item_detail, name='item_detail'),
]