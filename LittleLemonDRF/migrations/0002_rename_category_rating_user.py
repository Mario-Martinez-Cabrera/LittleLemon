# Generated by Django 4.1.7 on 2023-03-03 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonDRF', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='category',
            new_name='user',
        ),
    ]
