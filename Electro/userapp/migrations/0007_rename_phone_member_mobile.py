# Generated by Django 4.1.3 on 2023-02-15 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_member_delete_userregmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='phone',
            new_name='mobile',
        ),
    ]
