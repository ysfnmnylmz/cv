# Generated by Django 2.2.2 on 2019-06-13 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0050_auto_20190613_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='title',
            field=models.CharField(choices=[('Facebook-f', 'facebook-f'), ('Twitter', 'twitter'), ('Instagram', 'instagram'), ('Whatsapp', 'whatsapp'), ('youtube', 'youtube')], max_length=99, verbose_name='Select Social Media'),
        ),
    ]