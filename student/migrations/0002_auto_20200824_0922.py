# Generated by Django 3.1 on 2020-08-24 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
