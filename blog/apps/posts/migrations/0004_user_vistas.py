# Generated by Django 5.1.2 on 2024-10-25 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_user_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='vistas',
            field=models.IntegerField(default=0),
        ),
    ]
