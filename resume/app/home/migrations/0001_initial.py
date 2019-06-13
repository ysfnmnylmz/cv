# Generated by Django 2.2.2 on 2019-06-10 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank='False', max_length=55, verbose_name='Name and Surname')),
                ('degree', models.CharField(blank='False', max_length=55, verbose_name='Your Position')),
                ('image', models.ImageField(upload_to='')),
                ('birthday', models.DateField()),
                ('placeofbirth', models.CharField(max_length=55, verbose_name='Place of Birth')),
                ('mail', models.EmailField(blank='False', max_length=254, verbose_name='Your Mail Adress')),
                ('phone', models.IntegerField(blank='True', verbose_name='Your Phone Number')),
            ],
        ),
    ]
