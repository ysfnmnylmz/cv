# Generated by Django 2.2.2 on 2019-06-11 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_personalinfo_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinfo',
            name='city',
        ),
    ]
