# Generated by Django 2.2.4 on 2020-03-18 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mal2_db', '0005_auto_20200221_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(help_text='Enter url of the reviewing website', max_length=2000, null=True, verbose_name='URL')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3, null=True, verbose_name='Rating')),
                ('assigned_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Assigned to')),
            ],
        ),
    ]
