# Generated by Django 2.2.2 on 2019-06-11 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_education_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='department',
            field=models.CharField(default='', max_length=255, verbose_name='Department Name'),
        ),
    ]
