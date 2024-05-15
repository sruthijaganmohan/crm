# Generated by Django 5.0.3 on 2024-03-26 14:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_comment'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_comments', to='team.team'),
        ),
    ]