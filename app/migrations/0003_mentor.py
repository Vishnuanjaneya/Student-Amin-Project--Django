# Generated by Django 5.0.6 on 2024-06-25 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_students_mentor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Mentor', models.CharField(max_length=30)),
                ('TimeSlot', models.CharField(max_length=30)),
            ],
        ),
    ]
