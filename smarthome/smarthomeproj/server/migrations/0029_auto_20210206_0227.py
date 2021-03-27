# Generated by Django 3.1.3 on 2021-02-06 02:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('server', '0028_auto_20210205_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housekey',
            name='key',
            field=models.CharField(blank=True, default='3885370972', editable=False, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
