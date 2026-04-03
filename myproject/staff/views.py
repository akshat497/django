from django.shortcuts import render
from .models import Staff
from django.http import JsonResponse as jsonResponse
# Create your views here.
def staff_list(request):
    staff=Staff.objects.all()
    return render(request, 'staffList.html', )



def activeStaff(request):
    staff=Staff.objects.filter(salary__gt=50000)
    return render(request, 'activeStaff.html', {'staff_list': staff})