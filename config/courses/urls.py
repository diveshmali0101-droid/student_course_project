from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('signup/', views.signup, name='signup'),
    path('update-username/', views.update_username, name='update_username'),
    path('enroll/<int:course_id>/', views.enroll_course, name='enroll'),
    path('my-courses/', views.my_courses, name='my_courses'),
]
