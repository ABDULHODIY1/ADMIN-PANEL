# Generated by Django 4.2.4 on 2023-08-09 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField(blank=True, max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('Text', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PANTERAUSERS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('user_name', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
