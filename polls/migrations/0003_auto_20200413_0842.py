# Generated by Django 3.0.5 on 2020-04-13 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200413_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='publish_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]