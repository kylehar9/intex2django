# Generated by Django 3.0.3 on 2020-04-09 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200407_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='campaign_image_url',
            field=models.TextField(null=True),
        ),
    ]
