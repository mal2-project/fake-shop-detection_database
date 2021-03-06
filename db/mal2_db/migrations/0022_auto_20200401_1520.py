# Generated by Django 2.2.4 on 2020-04-01 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mal2.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mal2_db', '0021_auto_20200401_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='created_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_mal2_db_website_set', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='website',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modified_mal2_db_website_set', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
        migrations.AlterField(
            model_name='website',
            name='created',
            field=mal2.models.fields.CreationDateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='website',
            name='modified',
            field=mal2.models.fields.ModificationDateTimeField(auto_now=True, verbose_name='Modified'),
        ),
    ]
