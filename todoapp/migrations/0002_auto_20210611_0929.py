# Generated by Django 3.1.7 on 2021-06-11 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('C', 'COMPLETE'), ('p', 'PENDING')], max_length=2),
        ),
    ]
