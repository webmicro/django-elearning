# Generated by Django 4.0.5 on 2022-08-02 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_online', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experts',
            name='fb_url',
            field=models.URLField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experts',
            name='ins_url',
            field=models.URLField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experts',
            name='tw_url',
            field=models.URLField(max_length=255, null=True),
        ),
    ]
