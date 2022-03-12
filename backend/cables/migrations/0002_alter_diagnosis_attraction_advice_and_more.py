# Generated by Django 4.0.3 on 2022-03-12 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cables", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="diagnosis",
            name="attraction_advice",
            field=models.BooleanField(
                default=False, null=True, verbose_name="Attraction"
            ),
        ),
        migrations.AlterField(
            model_name="diagnosis",
            name="dissuasion_advice",
            field=models.BooleanField(
                default=False, null=True, verbose_name="Disruption"
            ),
        ),
        migrations.AlterField(
            model_name="diagnosis",
            name="isolation_advice",
            field=models.BooleanField(
                default=False, null=True, verbose_name="Isolation"
            ),
        ),
    ]
