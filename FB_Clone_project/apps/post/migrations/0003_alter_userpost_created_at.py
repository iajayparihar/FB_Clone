# Generated by Django 5.0.3 on 2024-04-10 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
