# Generated by Django 3.2.7 on 2021-09-16 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votation', '0003_auto_20210914_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='ramenya',
            name='total_votes',
            field=models.PositiveBigIntegerField(blank=True, default=0),
        ),
        migrations.DeleteModel(
            name='RamenScore',
        ),
    ]