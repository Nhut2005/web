# Generated by Django 5.1.4 on 2025-01-03 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('T_package_Mng', '0002_infortransport'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
