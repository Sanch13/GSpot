# Generated by Django 4.2.2 on 2023-06-13 15:20

import developer.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0004_alter_company_options_alter_companycontact_options_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='companyuser',
            managers=[
                ('objects', developer.models.CompanyUserManager()),
            ],
        ),
    ]
