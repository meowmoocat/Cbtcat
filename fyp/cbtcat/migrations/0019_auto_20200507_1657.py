# Generated by Django 3.0.3 on 2020-05-07 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtcat', '0018_l1a'),
    ]

    operations = [
        migrations.AlterField(
            model_name='l1a',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='l1a',
            name='finished_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]