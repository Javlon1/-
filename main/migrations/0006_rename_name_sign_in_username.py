# Generated by Django 3.2.9 on 2022-05-22 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220522_2119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sign_in',
            old_name='name',
            new_name='username',
        ),
    ]
