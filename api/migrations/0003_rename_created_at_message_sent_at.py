# Generated by Django 3.2.6 on 2021-10-07 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211005_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='created_at',
            new_name='sent_at',
        ),
    ]
