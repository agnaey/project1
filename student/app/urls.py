from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index_page),
    path('add',views.add_std),
    path('view',views.view_std),
    path('update',views.update_std),
    path('edit',views.edit_std),
]