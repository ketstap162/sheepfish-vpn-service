# Generated by Django 4.2.7 on 2023-11-14 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("VPN", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="site",
            name="alias",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="site",
            name="url",
            field=models.URLField(),
        ),
    ]