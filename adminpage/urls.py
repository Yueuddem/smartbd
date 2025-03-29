from django.urls import path
from django.contrib import admin 
from adminpage import views 
from .views import *
from .api import *
app_name = 'adminpage'

urlpatterns = [
    path('view/<str:model_name>/', dynamic_index, name="dynamic_index"),
    path('view/<str:model_name>/add/', dynamic_add, name="dynamic_add"),
    path('view/<str:model_name>/edit/<int:id>/', dynamic_edit, name="dynamic_edit"),
    path('view/<str:model_name>/delete/<int:id>/', dynamic_delete, name="dynamic_delete"),
    
]  
