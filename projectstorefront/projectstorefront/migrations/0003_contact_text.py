# Generated by Django 3.2.15 on 2022-09-06 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectstorefront', '0002_remove_contact_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='text',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
