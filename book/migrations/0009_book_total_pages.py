# Generated by Django 5.2 on 2025-05-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_bookmark'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_pages',
            field=models.IntegerField(default=0),
        ),
    ]
