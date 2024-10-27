from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index_page),
    path('add',views.add_std),
    path('view',views.view_std),
    path('update/',views.update_std),
    path('edit/<roll>',views.edit_std),
    path('delete/<roll>',views.delete_std),
    # path('search/<roll>',views.search_std),
]