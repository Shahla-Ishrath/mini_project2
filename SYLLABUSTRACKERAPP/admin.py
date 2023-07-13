from django.contrib import admin
from .models import course,day,syllabus,course_syllabus

# Register your models here.

admin.site.register(course)
admin.site.register(day)
admin.site.register(syllabus)
admin.site.register(course_syllabus)





