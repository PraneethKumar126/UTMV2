# Generated by Django 4.2 on 2023-09-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HashTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashCode', models.CharField(max_length=250, unique=True)),
                ('link', models.TextField()),
            ],
        ),
    ]
