# Generated by Django 4.2 on 2024-11-22 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_feedback_sentiment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='sentiment',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
