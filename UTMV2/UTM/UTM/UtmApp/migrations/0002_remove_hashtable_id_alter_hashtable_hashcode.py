# Generated by Django 4.2 on 2023-09-15 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UtmApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hashtable',
            name='id',
        ),
        migrations.AlterField(
            model_name='hashtable',
            name='hashCode',
            field=models.CharField(max_length=250, primary_key=True, serialize=False, unique=True),
        ),
    ]
