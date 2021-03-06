# Generated by Django 2.2.4 on 2020-02-21 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mal2_db', '0003_auto_20200220_1515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='searchresult',
            options={'verbose_name': 'Search result', 'verbose_name_plural': 'Enter URLs for search results'},
        ),
        migrations.AlterField(
            model_name='websitetext',
            name='website_text_url',
            field=models.URLField(blank=True, help_text='URL of the checked text', max_length=2000, null=True, verbose_name='URL'),
        ),
    ]
