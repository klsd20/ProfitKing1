# Generated by Django 4.0.4 on 2022-05-12 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocksapi', '0007_user1_digi_pin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user1',
            name='digi_pin',
        ),
    ]
