# Generated by Django 4.2 on 2023-09-16 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UtmApp', '0002_remove_hashtable_id_alter_hashtable_hashcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtable',
            name='link',
            field=models.TextField(null=True),
        ),
    ]
