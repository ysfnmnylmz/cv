# Generated by Django 2.2.2 on 2019-06-11 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_auto_20190611_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=255, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Footer Text',
                'verbose_name_plural': '4 - Footer Texts',
            },
        ),
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['section__title', 'title'], 'verbose_name': 'Content', 'verbose_name_plural': '3 - Contents'},
        ),
        migrations.AlterModelOptions(
            name='personalinfo',
            options={'verbose_name': 'Personal Info', 'verbose_name_plural': '1 - Personal Infos'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['title'], 'verbose_name': 'Section', 'verbose_name_plural': '2 - Sections'},
        ),
    ]
