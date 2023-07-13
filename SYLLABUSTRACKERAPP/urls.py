from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index),
    path('course/',views.course),
    path('coursesyllabus/',views.coursesyllabus),
    path('day/',views.day),
    path('syllabus/',views.syllabus),
 

    
]
