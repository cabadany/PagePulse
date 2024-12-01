<<<<<<< HEAD
# Generated by Django 5.1.1 on 2024-12-01 15:20
=======
# Generated by Django 5.1.2 on 2024-12-01 14:08
>>>>>>> 30173c3191e33a83ba24362abc75d7a83d5c6d97

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_remove_book_cover_image_book_book_image_and_more'),
        ('mylibrary', '0002_userlibrary_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlibrary',
            name='current_chapter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.chapter'),
        ),
        migrations.AddField(
            model_name='userlibrary',
            name='current_page',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
