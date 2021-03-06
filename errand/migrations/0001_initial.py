# Generated by Django 2.2.5 on 2019-10-21 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otsukai', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Errand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('deadline', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('image', models.FileField(upload_to='')),
                ('description', models.TextField(blank=True, help_text='依頼内容を記載してください．', max_length=1000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otsukai.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'errand',
            },
        ),
    ]
