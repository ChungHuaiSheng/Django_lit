# Generated by Django 4.1 on 2022-10-14 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Path",
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
                ("part_id", models.CharField(max_length=6)),
                ("reticle_id", models.CharField(max_length=10)),
                ("eqp_id", models.CharField(max_length=6)),
                ("lot_id", models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name="Tracer",
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
                    "trace_path",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tracer.path"
                    ),
                ),
            ],
        ),
    ]