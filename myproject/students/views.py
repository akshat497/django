from django.shortcuts import render
from .models import Student
from django.http import JsonResponse as jsonResponse
# Create your views here.


def student_list(request):
    student=Student.objects.all()
    return render(request, 'student_list.html', {'student_list': student})



    