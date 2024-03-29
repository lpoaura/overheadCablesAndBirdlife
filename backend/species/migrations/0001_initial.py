# Generated by Django 4.0.3 on 2022-03-16 08:50

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Species",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        max_length=100,
                        unique=True,
                        verbose_name="Species code",
                    ),
                ),
                (
                    "scientific_name",
                    models.CharField(
                        max_length=200, verbose_name="Scientific name"
                    ),
                ),
                (
                    "vernacular_name",
                    models.CharField(
                        max_length=200, verbose_name="Vernacular name"
                    ),
                ),
                (
                    "active",
                    models.BooleanField(default=True, verbose_name="Active"),
                ),
            ],
            options={
                "verbose_name_plural": "Species",
            },
        ),
    ]
