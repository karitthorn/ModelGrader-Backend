# Generated by Django 4.1.2 on 2023-12-11 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_alter_submissiontestcase_testcase'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcase',
            name='depricated',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]