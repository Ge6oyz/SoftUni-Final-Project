# Generated by Django 3.1.3 on 2020-12-02 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20201202_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='friends',
            field=models.ManyToManyField(related_name='_usermodel_friends_+', to='base.UserModel'),
        ),
    ]
