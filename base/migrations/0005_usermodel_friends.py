# Generated by Django 3.1.3 on 2020-12-01 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20201201_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='friends',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.usermodel'),
        ),
    ]
