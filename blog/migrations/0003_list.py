# Generated by Django 5.0 on 2023-12-17 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_subtitle_post_writer'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('writer', models.CharField(max_length=200)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]