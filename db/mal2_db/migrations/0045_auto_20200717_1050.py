# Generated by Django 2.2.4 on 2020-07-17 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mal2_db', '0044_auto_20200716_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='screenshot',
            field=models.FilePathField(blank=True, null=True, path='/data/git/mal2-ui/db/media/websites/screenshots'),
        ),
    ]
