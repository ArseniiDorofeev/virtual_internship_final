# Generated by Django 5.0.1 on 2024-01-29 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]
