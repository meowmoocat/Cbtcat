# Generated by Django 3.0.3 on 2020-05-07 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbtcat', '0016_auto_20200507_1213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lvl1answer',
            old_name='cbtcat_user_id',
            new_name='cbtcat_user',
        ),
    ]