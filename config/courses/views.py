from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UsernameUpdateForm
from .models import Course, Enrollment


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'courses/signup.html', {'form': form})


@login_required
def update_username(request):
    if request.method == 'POST':
        form = UsernameUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UsernameUpdateForm(instance=request.user)
    return render(request, 'courses/update_username.html', {'form': form})


@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


@login_required
def enroll_course(request, course_id):
    Enrollment.objects.get_or_create(
        student=request.user,
        course_id=course_id
    )
    return redirect('/')


@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'courses/my_courses.html', {'enrollments': enrollments})
