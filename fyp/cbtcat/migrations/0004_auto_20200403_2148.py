# Generated by Django 3.0.3 on 2020-04-03 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cbtcat', '0003_auto_20200403_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cbtcatuser',
            name='lvl_2',
            field=models.ForeignKey(help_text='Users lvl 2 info', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cbtcat.Lvl2Answer'),
        ),
        migrations.AlterField(
            model_name='cbtcatuser',
            name='lvl_3',
            field=models.ForeignKey(help_text='Users lvl 3 info', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cbtcat.Lvl3Answer'),
        ),
        migrations.AlterField(
            model_name='cbtcatuser',
            name='lvl_4',
            field=models.ForeignKey(help_text='Users lvl 4 info', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cbtcat.Lvl4Answer'),
        ),
        migrations.AlterField(
            model_name='cbtcatuser',
            name='lvl_5',
            field=models.ForeignKey(help_text='Users lvl 5 info', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cbtcat.Lvl5Answer'),
        ),
        migrations.AlterField(
            model_name='cbtcatuser',
            name='lvl_6',
            field=models.ForeignKey(help_text='Users lvl 6 info', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cbtcat.Lvl6Answer'),
        ),
    ]
