# Generated by Django 2.1 on 2018-08-12 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0010_auto_20180810_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliance',
            name='colour',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='appliance',
            name='depth',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='mm', max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='appliance',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='mm', max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='appliance',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='appliance',
            name='model',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='appliance',
            name='photo_3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='appliance',
            name='photo_4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='appliance',
            name='photo_5',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='appliance',
            name='photo_6',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='appliance',
            name='width',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='mm', max_digits=7, null=True),
        ),
    ]