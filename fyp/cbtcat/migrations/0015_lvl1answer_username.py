# Generated by Django 3.0.3 on 2020-05-06 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtcat', '0014_lvl1answer_current_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='lvl1answer',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
