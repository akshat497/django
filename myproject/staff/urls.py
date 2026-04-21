

from django.urls import path
from . import views

urlpatterns = [
     path('set_session/', views.set_session, name='set_session'),
    path('get_session/', views.get_session, name='get_session'),
    path('set_cookie/', views.set_cookie, name='set_cookie'),
    path('get_cookie/', views.get_cookie, name='get_cookie'),
    path('',views.staff_list, name='list'),
    path('add/', views.add_staff, name='add'),
    path('active/',views.activeStaff, name='active'),
    path('delete/<int:staff_id>/',views.delete_staff, name='delete'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('users/', views.user_list, name='user_list'),
   

]