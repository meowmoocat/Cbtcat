# Generated by Django 3.0.3 on 2020-05-08 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtcat', '0022_auto_20200508_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lvl2UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_unique_users_started', models.IntegerField(default=0)),
                ('num_unique_users_completed', models.IntegerField(default=0)),
                ('total_times_started', models.IntegerField(default=0)),
                ('total_times_finished', models.IntegerField(default=0)),
            ],
        ),
    ]
