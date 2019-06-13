# Generated by Django 2.2.2 on 2019-06-12 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_auto_20190612_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='title',
            field=models.CharField(choices=[('facebook', 'facebook'), ('twitter', 'twitter'), ('instagram', 'instagram'), ('whatsapp', 'whatsapp')], max_length=99, verbose_name='Select Social Media'),
        ),
    ]