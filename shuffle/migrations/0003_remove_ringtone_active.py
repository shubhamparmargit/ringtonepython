# Generated by Django 4.2.16 on 2024-09-30 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shuffle', '0002_remove_ringtone_rate_avg_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ringtone',
            name='active',
        ),
    ]