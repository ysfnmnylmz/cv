# Generated by Django 2.2.2 on 2019-06-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0046_auto_20190612_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='title',
            field=models.CharField(choices=[('Facebook', 'facebook'), ('Twitter', 'twitter'), ('Instagram', 'instagram'), ('Whatsapp', 'whatsapp')], max_length=99, verbose_name='Select Social Media'),
        ),
    ]
