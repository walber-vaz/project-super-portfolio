# Generated by Django 4.2.3 on 2023-09-16 14:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_certifyinginstitution_certificate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certifyinginstitution",
            name="name",
            field=models.CharField(
                max_length=100,
                validators=[
                    django.core.validators.MaxLengthValidator(limit_value=100)
                ],
            ),
        ),
    ]
