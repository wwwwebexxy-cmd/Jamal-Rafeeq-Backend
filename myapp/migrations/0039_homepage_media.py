# Generated manually for the editable homepage video slots.

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0038_optional_hero_banner_copy"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomepageMedia",
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
                    "brand_showcase_video",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="homepage_media/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["mp4", "webm", "ogg"]
                            )
                        ],
                    ),
                ),
                (
                    "global_reach_portrait_video",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="homepage_media/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["mp4", "webm", "ogg"]
                            )
                        ],
                    ),
                ),
                (
                    "global_reach_landscape_video",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="homepage_media/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["mp4", "webm", "ogg"]
                            )
                        ],
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ("id",)},
        ),
    ]
