# Generated by Django 3.1.5 on 2021-01-12 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=191, unique=True)),
                ('value', models.TextField()),
                ('category', models.CharField(max_length=191)),
                ('field_type', models.CharField(choices=[('STR', 'string'), ('INT', 'integer'), ('BLN', 'boolean'), ('TXT', 'text'), ('FIL', 'file')], default='STR', max_length=3)),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
