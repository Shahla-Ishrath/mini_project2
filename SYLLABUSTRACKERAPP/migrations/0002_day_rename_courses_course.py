# Generated by Django 4.2.3 on 2023-07-08 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SYLLABUSTRACKERAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=250)),
                ('Active', models.BooleanField()),
            ],
        ),
        migrations.RenameModel(
            old_name='courses',
            new_name='course',
        ),
    ]