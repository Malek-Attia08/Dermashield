# Generated by Django 5.1.1 on 2024-11-24 21:00

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event_title', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(5, 'Title must be at least 5 characters long.')])),
                ('event_Type', models.CharField(choices=[('Health Screening', 'Health Screening'), ('Wellness Workshop', 'Wellness Workshop'), ('Community Talk', 'Community Talk'), ('Awareness Campaign', 'Awareness Campaign'), ('Fitness Class', 'Fitness Class'), ('Support Group', 'Support Group')], help_text='Choose event type from the list.', max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('location', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Location should not contain special characters.', regex='^[a-zA-Z0-9\\s,.-]*$')])),
                ('affiche', models.FileField(upload_to='files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpeg', 'jpg'])])),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.CharField(max_length=1)),
                ('number', models.IntegerField()),
                ('is_booked', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='EventApp.event')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('seat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='EventApp.seat')),
            ],
        ),
    ]
