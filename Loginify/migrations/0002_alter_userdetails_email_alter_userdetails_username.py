# Generated by Django 5.1.2 on 2024-10-14 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loginify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='username',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
