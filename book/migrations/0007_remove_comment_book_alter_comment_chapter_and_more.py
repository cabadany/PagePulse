# Generated by Django 5.1.2 on 2024-12-01 18:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_comment_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='book',
        ),
        migrations.AlterField(
            model_name='comment',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='book.chapter'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
