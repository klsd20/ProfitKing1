# Generated by Django 4.0.4 on 2022-05-23 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocksapi', '0019_alter_holdings_avg_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='holdings',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
