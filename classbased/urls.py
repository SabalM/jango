from django.contrib import admin
from django.urls import path
from classbased import views

urlpatterns = [
    path('',views.LaptopListView.as_view(),name='laptop-list'),
    path('make',views.LaptopCreateView.as_view(),name='laptop-make'),
    path('<int:pk>/update',views.LaptopUpdateView.as_view(),name='laptop-update'),
    path('<int:pk>/delete',views.LaptopDeleteView.as_view(),name='laptop-delete'),
]