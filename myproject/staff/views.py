from django.shortcuts import redirect, render
from .models import Staff
from django.http import JsonResponse as jsonResponse
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request, 'home.html')
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, "Registration successful. Please log in.")
      
            return redirect('user_list')
            
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
def staff_list(request):
    staff=Staff.objects.all()
    return render(request, 'staffList.html',{"staff_list": staff} )

def user_list(request):
    users=User.objects.all()
    return render(request, 'userList.html', {'users': users})
def activeStaff(request):
    staff=Staff.objects.filter(salary__gt=50000)
    return render(request, 'activeStaff.html', {'staff_list': staff})



def add_staff(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        salary = request.POST.get('salary')
        email = request.POST.get('email')
        Staff.objects.create(name=name, age=age, salary=salary, email=email)
        return jsonResponse({'message': 'Staff added successfully'})
    return render(request, 'addStaff.html')


def delete_staff(request, staff_id):
    try:
        staff = Staff.objects.get(staff_id=staff_id)
        staff.delete()
        return jsonResponse({'message': 'Staff deleted successfully'})
    except Staff.DoesNotExist:
        return jsonResponse({'message': 'Staff not found'}, status=404)
    
