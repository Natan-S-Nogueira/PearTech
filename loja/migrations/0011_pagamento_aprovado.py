# Generated by Django 4.2.16 on 2024-11-01 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0010_pagamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagamento',
            name='aprovado',
            field=models.BooleanField(default=False),
        ),
    ]