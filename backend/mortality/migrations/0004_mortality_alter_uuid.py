# Generated by Django 4.2.7 on 2024-02-22 08:44

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mortality", "0003_mortality_gen_uuid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mortality",
            name="uuid",
            field=models.UUIDField(
                blank=True, default=uuid.uuid4, null=True, unique=True
            ),
        ),
    ]
