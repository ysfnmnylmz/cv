# Generated by Django 2.2.2 on 2019-06-11 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20190611_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='image',
            field=models.ImageField(blank='False', upload_to=''),
        ),
    ]
