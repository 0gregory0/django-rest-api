# Generated by Django 4.1.2 on 2022-10-07 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("street", models.CharField(max_length=250)),
                ("suite", models.CharField(max_length=250)),
                ("city", models.CharField(max_length=250)),
                ("zipcode", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=250)),
                ("catchPhrase", models.TextField()),
                ("bs", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Geo",
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
                ("lat", models.FloatField(max_length=10)),
                ("lng", models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=250)),
                ("username", models.CharField(max_length=250)),
                ("email", models.EmailField(max_length=250)),
                ("phone", models.CharField(max_length=30)),
                ("website", models.CharField(max_length=250)),
                (
                    "address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="db_app.address"
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="db_app.company"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="address",
            name="geo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="db_app.geo"
            ),
        ),
    ]
