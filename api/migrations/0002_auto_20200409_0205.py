# Generated by Django 3.0.3 on 2020-04-09 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='time_of_day',
            field=models.TextField(),
        ),
    ]