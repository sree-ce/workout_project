# Generated by Django 4.0.4 on 2022-05-03 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_trainer_certification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainer', to=settings.AUTH_USER_MODEL),
        ),
    ]
