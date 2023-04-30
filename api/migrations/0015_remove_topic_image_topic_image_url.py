# Generated by Django 4.1.2 on 2022-12-05 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_topic_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='image',
        ),
        migrations.AddField(
            model_name='topic',
            name='image_url',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]