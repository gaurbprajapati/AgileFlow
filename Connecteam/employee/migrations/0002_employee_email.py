# Generated by Django 3.2.5 on 2023-08-07 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.CharField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]