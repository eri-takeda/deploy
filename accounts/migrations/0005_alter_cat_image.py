# Generated by Django 5.0.6 on 2024-06-03 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_cat_user_recruiting_messagehistory_cat_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
