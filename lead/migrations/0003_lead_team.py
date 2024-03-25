# Generated by Django 5.0.3 on 2024-03-25 12:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0002_alter_lead_options_lead_converted_to_client_and_more'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leads', to='team.team'),
        ),
    ]
