# Generated by Django 3.2.4 on 2021-06-07 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='profile_id',
        ),
    ]
