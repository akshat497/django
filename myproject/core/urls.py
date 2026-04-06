from django.urls import path
from . import views


urlpatterns=[
    path('', views.student_list, name='list'),
    path('add/', views.add_student, name='add'),
    path('delete/<int:id>/', views.delete_student, name='delete'),
    path('edit/<int:id>/', views.edit_student, name='edit'),
]


# student.all()
# student.filter(age=25)
# student.filter(age__gt=20)  # age > 20
# student.filter(age__lt=30)  # age < 30
# student.filter(name__icontains='ak')# name contains 'ak' (case-ins
# student.order_by('age')  # order by age ascending
# student.objects.order_by('-age')  # order by age descending
# student.objects.reverse()
# student.objects.count()  # count of students
# student.objects.first()  # first student
# student.objects.last()  # last student
# student.objects.get(id=1)  # get student with id=1
# student.objects.distinct()
# student.objects.all()[:5]
# student.obects.all()[5:10]
# student.objects.all()[::2]

# student.objects.aggregate(Avg('age'))  # average age
# student.objects.aggregate(Max('age'))  # maximum age
# student.objects.aggregate(Min('age'))  # minimum age
# student.objects.aggregate(Sum('age'))  # sum of ages

# student.objects.create(name='John Doe', age=25, email='john@example.com')

# students.objects.filter(age__gt=20).update(name="new_name")

# # increment age by 1 for students older than 20

# student.objects.filter(id=1).delete()

# course.objects.select_related('student') # for foreign key relationships