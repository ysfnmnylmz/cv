# Generated by Django 2.2.2 on 2019-06-11 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190610_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='city',
            field=models.CharField(blank='True', max_length=55, verbose_name='City'),
        ),
    ]