# Generated by Django 3.2 on 2021-04-23 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='name'),
        ),
    ]