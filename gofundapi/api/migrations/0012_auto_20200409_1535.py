# Generated by Django 3.0.3 on 2020-04-09 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_campaign_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='score',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=20),
        ),
    ]