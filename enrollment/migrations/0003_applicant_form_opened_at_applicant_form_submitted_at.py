# Generated by Django 5.0.1 on 2024-01-17 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0002_applicant_social_media_handle_x_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='form_opened_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='form_submitted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
