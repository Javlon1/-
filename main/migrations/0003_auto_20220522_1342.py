# Generated by Django 3.2.9 on 2022-05-22 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220521_1506'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sign_in',
        ),
        migrations.RenameField(
            model_name='our_areas',
            old_name='text',
            new_name='text1',
        ),
        migrations.RemoveField(
            model_name='our_team',
            name='rating',
        ),
        migrations.AddField(
            model_name='our_areas',
            name='text2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
