# Generated by Django 4.2 on 2023-05-06 13:05

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('dateCreated', models.DateField()),
                ('duration', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('oldPrice', models.FloatField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=20)),
            ],
            options={
                'base_manager_name': 'objects',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salaire', models.FloatField()),
                ('grade', models.CharField(max_length=20)),
                ('specialty', models.CharField(max_length=255)),
                ('user_profile', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning_app.usermodel')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=20)),
                ('user_profile', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning_app.usermodel')),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_app.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_app.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_app.teacher'),
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='chapter_images/')),
                ('video', models.FileField(upload_to='chapter_videos/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_app.course')),
            ],
        ),
    ]
