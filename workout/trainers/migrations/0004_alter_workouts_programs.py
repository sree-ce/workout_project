# Generated by Django 4.0.4 on 2022-04-29 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0001_initial'),
        ('trainers', '0003_alter_workouts_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workouts',
            name='programs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admins.programs'),
        ),
    ]