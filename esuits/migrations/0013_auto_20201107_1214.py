# Generated by Django 3.0.8 on 2020-11-07 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esuits', '0012_auto_20201107_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='answer',
            field=models.TextField(blank=True, null=True, verbose_name=''),
        ),
    ]
