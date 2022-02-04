# Generated by Django 4.0.1 on 2022-02-03 09:24

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mortality", "0004_alter_mortality_data_source"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mortality",
            options={
                "verbose_name": "Mortality case",
                "verbose_name_plural": "Mortality cases",
            },
        ),
        migrations.AddField(
            model_name="mortality",
            name="geom",
            field=django.contrib.gis.db.models.fields.PointField(
                null=True, srid=4326
            ),
        ),
    ]