# Generated by Django 5.1.1 on 2024-11-25 18:49

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_wastecollectionrequest_collector_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wastecollectionrequest',
            name='booking_id',
            field=models.AutoField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]