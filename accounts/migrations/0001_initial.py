# Generated by Django 2.2.5 on 2019-10-21 08:02

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=100, verbose_name='User Name')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
                ('address', models.CharField(max_length=1024, verbose_name='Address')),
                ('age', models.CharField(max_length=256, verbose_name='Age')),
                ('gender', models.CharField(choices=[('man', '男性'), ('woman', '女性')], max_length=10, verbose_name='gender')),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', accounts.models.UserExtendManager()),
            ],
        ),
    ]
