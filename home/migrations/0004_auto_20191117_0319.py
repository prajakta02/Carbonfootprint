# Generated by Django 2.2.4 on 2019-11-17 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20191117_0149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='user',
            name='dist_bus_emission',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='dist_train_emission',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='electricity_emission',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='four_wheeler_emission',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='plastic_emission',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='trees_emission',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='two_wheeler_emission',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='dist_2',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='dist_4',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='dist_bus',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='dist_train',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='electricity',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='emission',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='fam',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='four_wheeler_mlg',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='four_wheeler_no',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='plastic',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='trees',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='two_wheeler_mlg',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='two_wheeler_no',
            field=models.FloatField(default=0),
        ),
    ]