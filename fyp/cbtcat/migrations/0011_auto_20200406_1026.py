# Generated by Django 3.0.3 on 2020-04-06 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cbtcat', '0010_auto_20200406_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lvl1answer',
            name='cbtcat_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cbtcat.CbtcatUser'),
        ),
    ]
