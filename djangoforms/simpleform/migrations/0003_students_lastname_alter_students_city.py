# Generated by Django 4.1 on 2022-09-05 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleform', '0002_rename_student_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='lastname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
