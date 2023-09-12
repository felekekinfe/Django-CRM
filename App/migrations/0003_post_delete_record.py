# Generated by Django 4.2.4 on 2023-09-06 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_record_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenet', models.TextField()),
                ('title', models.CharField(max_length=200)),
                ('posted_at', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Record',
        ),
    ]
