# Generated by Django 3.1.3 on 2021-02-03 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0019_auto_20210203_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housekey',
            name='key',
            field=models.CharField(blank=True, default='4997605086', editable=False, max_length=10, unique=True),
        ),
    ]
