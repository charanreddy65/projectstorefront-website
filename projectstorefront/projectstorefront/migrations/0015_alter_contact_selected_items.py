# Generated by Django 3.2.15 on 2022-09-19 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectstorefront', '0014_contact_selected_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='selected_items',
            field=models.CharField(choices=[], max_length=100),
        ),
    ]