# Generated by Django 3.1.3 on 2020-11-30 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20201130_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='image_url',
            field=models.URLField(default='https://genslerzudansdentistry.com/wp-content/uploads/2015/11/anonymous-user.png', null=True),
        ),
    ]
