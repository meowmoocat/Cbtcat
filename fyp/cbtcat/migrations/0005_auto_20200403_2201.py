# Generated by Django 3.0.3 on 2020-04-03 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtcat', '0004_auto_20200403_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lvl1answer',
            name='username',
        ),
        migrations.RemoveField(
            model_name='lvl2answer',
            name='username',
        ),
        migrations.RemoveField(
            model_name='lvl3answer',
            name='username',
        ),
        migrations.RemoveField(
            model_name='lvl4answer',
            name='username',
        ),
        migrations.RemoveField(
            model_name='lvl5answer',
            name='username',
        ),
        migrations.RemoveField(
            model_name='lvl6answer',
            name='username',
        ),
    ]
