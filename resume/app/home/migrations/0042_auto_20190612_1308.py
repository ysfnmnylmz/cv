# Generated by Django 2.2.2 on 2019-06-12 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_social'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='title',
            field=models.CharField(choices=[('facebook', 'Facebook'), ('twitter', 'Twitter'), ('instagram', 'Instagram'), ('whatsapp', 'Whatsapp')], max_length=99, verbose_name='Select Social Media'),
        ),
    ]
