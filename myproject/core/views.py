from django.shortcuts import render, redirect,get_object_or_404
from .models import Student

def add_student(request):
    error = None

    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']

        # ✅ check if email already exists
        if Student.objects.filter(email=email).exists():
            error = "Email already exists!"
        else:
            Student.objects.create(
                name=name,
                age=age,
                email=email
            )
            return redirect('list')

    return render(request, 'students/student_form.html', {'error': error})

def student_list(request):
    students = Student.objects.all()  # SELECT * FROM student
    return render(request, 'students/student_list.html', {'students': students})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('list')

def edit_student(request,id):
    student=get_object_or_404(Student, id=id)
    error=None
    if student.objects.filter(email=student.email).exclude(id=student.id).exists():
        error="Email already exists!"
    if request.method=="POST":
        student.name=request.POST['name']
        student.age=request.POST['age']
        student.email=request.POST['email']
        student.save()
        return redirect('list')
    return render(request, 'students/student_form.html', {'student':student,'error':error}) 