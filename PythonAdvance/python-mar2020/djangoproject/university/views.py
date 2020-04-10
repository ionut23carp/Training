from django.shortcuts import render, get_object_or_404

from .models import University, Student


def index(request):
    universities = University.objects.all()
    context = {'universities': universities}
    return render(request, 'university/index.html', context)


def university_details(request, university_id):
<<<<<<< Updated upstream
    university = get_object_or_404(University, pk=university_id)
    context = {'university': university}
=======
    university = University.objects.get(pk=university_id)
    students = Student.objects.filter(university=university)
    context = {'university': university, 'students': students}
>>>>>>> Stashed changes
    return render(request, 'university/university_details.html', context)


def student_details(request, student_id):
    student = Student.objects.get(pk=student_id)
    context = {'student': student}
<<<<<<< Updated upstream
    return render(request, 'university/student_details.html', context)
=======
    return render(request, 'student/student_details.html', context)
>>>>>>> Stashed changes
