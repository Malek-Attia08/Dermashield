# Generated by Django 4.2 on 2024-11-22 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_rename_customuser_feedback_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='sentiment',
            field=models.CharField(blank=True, choices=[('positive', 'Positive'), ('negative', 'Negative'), ('neutral', 'Neutral')], max_length=20, null=True),
        ),
    ]
