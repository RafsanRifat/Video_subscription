# Generated by Django 4.0 on 2021-12-14 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_coursemodule_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=200),
        ),
    ]
