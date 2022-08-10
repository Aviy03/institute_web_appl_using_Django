# Generated by Django 3.2.5 on 2022-07-26 20:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='queryid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
