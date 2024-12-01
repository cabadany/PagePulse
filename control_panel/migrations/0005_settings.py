# Generated by Django 5.1.1 on 2024-12-01 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0004_remove_book_description_book_book_image_book_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=100)),
                ('site_logo', models.ImageField(upload_to='logos/')),
                ('admin_email', models.EmailField(max_length=254)),
                ('contact_info', models.TextField()),
                ('theme', models.CharField(choices=[('light', 'Light'), ('dark', 'Dark')], max_length=20)),
            ],
        ),
    ]
