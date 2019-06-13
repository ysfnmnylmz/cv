# Generated by Django 2.2.2 on 2019-06-11 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20190611_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='department',
            field=models.CharField(default='', max_length=255, null=True, verbose_name='Department Name'),
        ),
        migrations.AlterField(
            model_name='education',
            name='faculty',
            field=models.CharField(max_length=255, null=True, verbose_name='Faculty Name'),
        ),
        migrations.AlterField(
            model_name='education',
            name='institution',
            field=models.CharField(max_length=255, null=True, verbose_name='Institution Name'),
        ),
        migrations.AlterField(
            model_name='education',
            name='type',
            field=models.CharField(choices=[('Born', 'Born'), ('First School', 'First School'), ('High School', 'High School'), ('University', 'University'), ('Master', 'Master')], default='', max_length=255, null=True, verbose_name='Select Data Type'),
        ),
    ]
