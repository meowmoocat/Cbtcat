# Generated by Django 3.0.3 on 2020-04-05 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cbtcat', '0008_auto_20200405_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lvl1answer',
            name='cbtcat_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cbtcat.CbtcatUser'),
        ),
        migrations.AlterField(
            model_name='lvl2answer',
            name='cbtcat_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cbtcat.CbtcatUser'),
        ),
        migrations.AlterField(
            model_name='lvl3answer',
            name='cbtcat_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cbtcat.CbtcatUser'),
        ),
        migrations.AlterField(
            model_name='lvl4answer',
            name='cbtcat_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cbtcat.CbtcatUser'),
        ),
        migrations.AlterField(
            model_name='lvl5answer',
            name='cbtcat_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cbtcat.CbtcatUser'),
        ),
        migrations.AlterField(
            model_name='lvl6answer',
            name='cbtcat_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cbtcat.CbtcatUser'),
        ),
    ]