# Generated by Django 5.1.7 on 2025-03-16 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="is_staff",
            field=models.BooleanField(default=True, verbose_name="Персонал"),
        ),
    ]
