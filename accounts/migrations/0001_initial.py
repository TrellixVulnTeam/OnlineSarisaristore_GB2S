# Generated by Django 3.1 on 2020-08-15 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=30, unique=True, verbose_name='email')),
                ('mobile', models.IntegerField(verbose_name='Mobile Number')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date joined')),
                ('last_login', models.DateTimeField(auto_now_add=True, verbose_name='Last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
