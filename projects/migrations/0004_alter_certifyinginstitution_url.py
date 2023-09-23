# Generated by Django 4.2.3 on 2023-09-16 14:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0003_alter_certifyinginstitution_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certifyinginstitution",
            name="url",
            field=models.URLField(
                validators=[django.core.validators.URLValidator()]
            ),
        ),
    ]