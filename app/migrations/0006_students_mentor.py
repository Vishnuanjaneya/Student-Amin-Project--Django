# Generated by Django 5.0.6 on 2024-07-05 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_mentor_timeslot'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='mentor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.mentor'),
        ),
    ]
