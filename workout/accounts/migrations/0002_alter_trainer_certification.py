# Generated by Django 4.0.4 on 2022-04-28 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='certification',
            field=models.CharField(choices=[('ISSA', 'ISSA'), ('NCSF', 'NCSF'), ('ACE', 'ACE'), ('FITNESS MENTORS', 'fitness mentors'), ('PG', 'PG'), ('B.Ed', 'B.Ed'), ('DIPLOMA ', 'diploma ')], max_length=250),
        ),
    ]
