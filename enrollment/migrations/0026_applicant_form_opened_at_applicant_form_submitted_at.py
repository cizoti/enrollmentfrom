# Generated by Django 5.0.1 on 2024-01-13 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0025_aim_checkboxoption_hearabout_checkboxoption_and_more'),
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