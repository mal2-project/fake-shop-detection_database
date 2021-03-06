# Generated by Django 2.2.4 on 2020-04-02 05:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mal2_db', '0034_auto_20200401_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mal2counterfeitersdb',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='mal2counterfeitersdb',
            old_name='modified',
            new_name='modified_at',
        ),
        migrations.RenameField(
            model_name='mal2fakeshopdb',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='mal2fakeshopdb',
            old_name='modified',
            new_name='modified_at',
        ),
        migrations.RenameField(
            model_name='website',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='website',
            old_name='modified',
            new_name='modified_at',
        ),
        migrations.RemoveField(
            model_name='website',
            name='reported_on',
        ),
        migrations.AddField(
            model_name='website',
            name='reported_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Reported at'),
            preserve_default=False,
        ),
    ]
