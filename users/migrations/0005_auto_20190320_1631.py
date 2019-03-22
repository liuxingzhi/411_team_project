# Generated by Django 2.1.7 on 2019-03-20 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190320_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='occupation',
            field=models.CharField(default='none', max_length=2000),
        ),
        migrations.AddField(
            model_name='profile',
            name='synopsis',
            field=models.CharField(default='none', max_length=2000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='GPA',
            field=models.FloatField(default=0.0),
        ),
    ]