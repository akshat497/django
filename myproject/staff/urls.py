from django.urls import path
from . import views

urlpatterns = [
    path('',views.staff_list, name='list'),
    path('active/',views.activeStaff, name='active'),
]