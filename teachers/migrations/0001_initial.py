# Generated by Django 5.0.6 on 2024-06-17 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.PositiveSmallIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=20)),
                ('id_number', models.PositiveSmallIntegerField()),
                ('subject', models.CharField(max_length=20)),
                ('years_of_experience', models.PositiveSmallIntegerField()),
                ('office_hours', models.PositiveSmallIntegerField()),
                ('office_room_number', models.PositiveSmallIntegerField()),
            ],
        ),
    ]