# Generated by Django 3.0.5 on 2020-04-07 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200407_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='days_active',
            field=models.IntegerField(blank=True),
        ),
    ]