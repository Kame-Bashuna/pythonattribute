# Generated by Django 5.0.7 on 2024-07-25 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_rename_capacity_class_class_numberof_student_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Class',
            new_name='Classes',
        ),
    ]