# Generated by Django 4.2.dev20220824103047 on 2022-09-03 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_rename_user_film_number_of_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='number_of_user',
            new_name='number_of_users',
        ),
    ]
