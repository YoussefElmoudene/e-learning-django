# Generated by Django 4.2 on 2023-05-06 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='orderNumber',
            field=models.FloatField(default=1),
        ),
    ]
