# Generated by Django 4.0.5 on 2022-08-16 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learn_online', '0013_course_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='total_student',
            field=models.IntegerField(choices=[(5, '5 Students'), (10, '10 Students'), (15, '15 Students'), (20, '20 Students'), (25, '25 Students'), (30, '30 Students')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn_online.experts'),
        ),
    ]
