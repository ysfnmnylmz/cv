# Generated by Django 2.2.2 on 2019-06-11 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20190611_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='graduation',
        ),
        migrations.AddField(
            model_name='education',
            name='type',
            field=models.CharField(choices=[('Born', 'Born'), ('College', 'College'), ('High School', 'High School'), ('University', 'University'), ('Master', 'Master')], default='', max_length=255, verbose_name='Select Data Type'),
        ),
    ]
