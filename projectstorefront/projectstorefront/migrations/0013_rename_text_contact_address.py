# Generated by Django 3.2.15 on 2022-09-17 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectstorefront', '0012_rename_address_contact_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='text',
            new_name='address',
        ),
    ]