# Generated by Django 3.0.5 on 2020-04-07 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200407_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='days_active',
            field=models.IntegerField(),
        ),
    ]
