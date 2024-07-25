# Generated by Django 5.0.6 on 2024-06-18 06:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carrer", "0003_casestudy_maincasestudy_testimonial"),
    ]

    operations = [
        migrations.AddField(
            model_name="testimonial",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="testimonials/"),
        ),
        migrations.AddField(
            model_name="testimonial",
            name="job",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="testimonial",
            name="linkedin",
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]