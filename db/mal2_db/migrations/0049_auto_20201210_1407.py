# Generated by Django 2.2.4 on 2020-12-10 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mal2_db', '0048_auto_20201202_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitetype',
            name='ordering_index',
            field=models.PositiveIntegerField(default=0, verbose_name='Ordering index'),
        ),
    ]