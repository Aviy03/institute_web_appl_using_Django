# Generated by Django 3.2.5 on 2022-07-18 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='fees',
            field=models.IntegerField(),
        ),
    ]
