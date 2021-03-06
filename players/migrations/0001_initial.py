# Generated by Django 3.1.3 on 2022-06-15 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('nationality', models.TextField()),
                ('date', models.TextField()),
                ('team', models.TextField(blank=True)),
                ('url', models.URLField()),
            ],
        ),
    ]
