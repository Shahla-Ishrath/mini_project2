# Generated by Django 4.2.1 on 2023-07-12 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SYLLABUSTRACKERAPP', '0004_course_syllabus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_syllabus',
            name='Active',
        ),
        migrations.AddField(
            model_name='course_syllabus',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SYLLABUSTRACKERAPP.course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course_syllabus',
            name='day',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SYLLABUSTRACKERAPP.day'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course_syllabus',
            name='syllabus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SYLLABUSTRACKERAPP.syllabus'),
        ),
    ]