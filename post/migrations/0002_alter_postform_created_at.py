# Generated by Django 5.0.2 on 2024-03-05 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postform',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
