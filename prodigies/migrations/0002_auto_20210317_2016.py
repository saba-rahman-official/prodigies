# Generated by Django 3.1.3 on 2021-03-17 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodigies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='due_date',
        ),
        migrations.AddField(
            model_name='meeting',
            name='date',
            field=models.CharField(default=-1, max_length=50),
        ),
        migrations.AddField(
            model_name='todo',
            name='due_time',
            field=models.CharField(default=-1, max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='time',
            field=models.CharField(max_length=50),
        ),
    ]
