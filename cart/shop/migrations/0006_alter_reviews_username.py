# Generated by Django 4.2.1 on 2023-05-11 15:51

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shop", "0005_cart_cart_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reviews",
            name="username",
            field=models.ForeignKey(
                default=django.contrib.auth.models.User,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
