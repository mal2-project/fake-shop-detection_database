# Generated by Django 2.2.4 on 2020-04-01 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mal2_db', '0031_auto_20200401_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mal2_db_website_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='website',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mal2_db_website_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
    ]
