# Generated by Django 2.2.2 on 2019-06-11 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_auto_20190611_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='section',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='content_section', to='home.Section', verbose_name='Section'),
        ),
    ]
