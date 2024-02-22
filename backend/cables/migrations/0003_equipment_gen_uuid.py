# Generated by Django 4.2.7 on 2024-02-22 08:43

import uuid

from django.db import migrations, models


def gen_uuid(apps, schema_editor):
    MyModel = apps.get_model("cables", "Equipment")
    for row in MyModel.objects.all():
        row.uuid = uuid.uuid4()
        row.save(update_fields=["uuid"])


class Migration(migrations.Migration):
    dependencies = [
        ("cables", "0002_equipment_uuid"),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]