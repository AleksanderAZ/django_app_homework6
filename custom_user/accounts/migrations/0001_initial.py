# Generated by Django 5.1.7 on 2025-03-15 09:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Пошта"
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        max_length=15, unique=True, verbose_name="Телефон"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(blank=True, max_length=30, verbose_name="Ім`я"),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=30, verbose_name="Прізвище"
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        blank=True, null=True, verbose_name="День  народження"
                    ),
                ),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="profile_picts/"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Активний"),
                ),
                (
                    "is_staff",
                    models.BooleanField(default=False, verbose_name="Персонал"),
                ),
                (
                    "date_joined",
                    models.DateField(
                        default=django.utils.timezone.now,
                        verbose_name="Дата реєстрації",
                    ),
                ),
                (
                    "preferred_language",
                    models.CharField(
                        choices=[("uk", "Українська"), ("en", "English")],
                        default="uk",
                        max_length=10,
                        verbose_name="Мова",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Користувач",
                "verbose_name_plural": "Користувачі",
                "permissions": [
                    ("can_view_profiles", "Переглядати профілі інших"),
                    ("can_edit_profiles", "Редагувати профілі інших"),
                ],
            },
        ),
    ]
