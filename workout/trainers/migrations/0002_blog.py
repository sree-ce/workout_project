# Generated by Django 4.0.4 on 2022-04-25 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blog_Title', models.CharField(max_length=250)),
                ('Content', models.TextField()),
                ('Select_image', models.ImageField(upload_to='')),
            ],
        ),
    ]