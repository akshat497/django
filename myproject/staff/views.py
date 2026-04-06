from django.shortcuts import render
from .models import Staff
from django.http import JsonResponse as jsonResponse
# Create your views here.
def staff_list(request):
    staff=Staff.objects.all()
    return render(request, 'staffList.html',{"staff_list": staff} )



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