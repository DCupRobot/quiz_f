# Generated by Django 2.2.2 on 2019-11-14 06:16

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
                ('user_name', models.CharField(max_length=31)),
                ('user_email', models.CharField(max_length=63)),
            ],
            options={
                'verbose_name': 'user info',
                'verbose_name_plural': 'user info',
                'db_table': 'user',
            },
        ),
    ]
