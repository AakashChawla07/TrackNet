# Generated by Django 5.2.2 on 2025-06-15 03:05

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_college_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='college_email',
            field=models.EmailField(max_length=254, unique=True, validators=[accounts.models.User.validate_thapar_email]),
        ),
    ]
