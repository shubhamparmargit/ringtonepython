# Generated by Django 4.2.16 on 2024-10-01 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shuffle', '0004_customuser_user_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='shuffle.city'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_all',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='ringtone_language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='shuffle.ringtone_language'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='shuffle.state'),
        ),
    ]
