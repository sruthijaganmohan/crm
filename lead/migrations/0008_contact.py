# Generated by Django 5.0.3 on 2024-04-01 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0007_comment_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=1000)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
