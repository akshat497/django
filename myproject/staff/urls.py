

from django.urls import path
from . import views

urlpatterns = [
    path('',views.staff_list, name='list'),
    path('add/', views.add_staff, name='add'),
    path('active/',views.activeStaff, name='active'),
    path('delete/<int:staff_id>/',views.delete_staff, name='delete'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('users/', views.user_list, name='user_list'),

]