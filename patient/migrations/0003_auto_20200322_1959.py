# Generated by Django 2.2.7 on 2020-03-22 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20200320_2358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='email',
            new_name='pemail',
        ),
    ]
