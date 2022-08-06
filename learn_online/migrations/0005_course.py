# Generated by Django 4.0.5 on 2022-08-06 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_online', '0004_experts_display_about_page_alter_experts_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=128)),
                ('fee', models.FloatField(max_length=20)),
                ('duration', models.CharField(max_length=100)),
                ('total_student', models.IntegerField(max_length=11)),
                ('trainer', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='courses/')),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
