# Generated by Django 3.0.3 on 2020-04-03 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CbtcatUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_times_login', models.IntegerField(default=1, help_text='Number of times the user has logged in')),
            ],
        ),
        migrations.CreateModel(
            name='Lvl6Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('finished', models.BooleanField(default=False)),
                ('finished_on', models.DateTimeField(blank=True, null=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cbtcat.CbtcatUsers')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Lvl5Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('finished', models.BooleanField(default=False)),
                ('finished_on', models.DateTimeField(blank=True, null=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cbtcat.CbtcatUsers')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Lvl4Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('finished', models.BooleanField(default=False)),
                ('finished_on', models.DateTimeField(blank=True, null=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cbtcat.CbtcatUsers')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Lvl3Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('finished', models.BooleanField(default=False)),
                ('finished_on', models.DateTimeField(blank=True, null=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cbtcat.CbtcatUsers')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Lvl2Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('finished', models.BooleanField(default=False)),
                ('finished_on', models.DateTimeField(blank=True, null=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cbtcat.CbtcatUsers')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Lvl1Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('finished', models.BooleanField(default=False)),
                ('finished_on', models.DateTimeField(blank=True, null=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cbtcat.CbtcatUsers')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.AddField(
            model_name='cbtcatusers',
            name='lvl_1',
            field=models.ForeignKey(help_text='Users lvl 1 info', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cbtcat.Lvl1Answers'),
        ),
        migrations.AddField(
            model_name='cbtcatusers',
            name='lvl_2',
            field=models.ForeignKey(help_text='Users lvl 1 info', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cbtcat.Lvl2Answers'),
        ),
        migrations.AddField(
            model_name='cbtcatusers',
            name='lvl_3',
            field=models.ForeignKey(help_text='Users lvl 1 info', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cbtcat.Lvl3Answers'),
        ),
        migrations.AddField(
            model_name='cbtcatusers',
            name='lvl_4',
            field=models.ForeignKey(help_text='Users lvl 1 info', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cbtcat.Lvl4Answers'),
        ),
        migrations.AddField(
            model_name='cbtcatusers',
            name='lvl_5',
            field=models.ForeignKey(help_text='Users lvl 1 info', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cbtcat.Lvl5Answers'),
        ),
        migrations.AddField(
            model_name='cbtcatusers',
            name='lvl_6',
            field=models.ForeignKey(help_text='Users lvl 1 info', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cbtcat.Lvl6Answers'),
        ),
        migrations.AddField(
            model_name='cbtcatusers',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
