# Generated by Django 5.1.1 on 2024-11-25 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_wastecollectionrequest_booking_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wastecollectionrequest',
            name='booking_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
