# Generated by Django 4.0.5 on 2022-08-11 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_online', '0010_alter_course_total_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('subject', models.CharField(max_length=128)),
                ('message', models.TextField()),
            ],
        ),
    ]
