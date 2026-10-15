from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0037_seed_product_fitments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="herobanner",
            name="subtitle",
            field=models.CharField(blank=True, default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="herobanner",
            name="title",
            field=models.CharField(blank=True, default="", max_length=200),
        ),
        migrations.AlterField(
            model_name="herobanner",
            name="description",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="herobanner",
            name="button_text",
            field=models.CharField(blank=True, default="Explore Collection", max_length=50),
        ),
    ]
