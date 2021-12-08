from django.shortcuts import render
from .forms import StudentForm
from .models import StudentModel
from statistics import mean


def add_student(request):

    form = StudentForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            grades_str = form.cleaned_data['grades']
            grades_int_list = list(map(int, grades_str.split(',')))
            avg_grade = mean(grades_int_list)

            student = StudentModel(
                name=form.cleaned_data['name'],
                grades=form.cleaned_data['grades'],
                average_grade=avg_grade,
            )

            student.save()

            context = {
                'student': student,
            }

            return render(
                request,
                template_name='student.html',
                context=context,
            )

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='add_student.html',
        context=context,
    )

def get_students(request):

    students = StudentModel.objects.all()

    context = {
        'students': students,
    }

    return render(
        request,
        template_name='students.html',
        context=context,
    )

def get_student(request, student_id):

    student = StudentModel.objects.get(id=student_id)

    context = {
        'student': student,
    }

    return render(
        request,
        template_name='student.html',
        context=context,
    )
