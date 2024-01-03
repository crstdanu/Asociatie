from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_apartment, name='view_apartment'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('view/<int:id>/', views.view, name='view'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
