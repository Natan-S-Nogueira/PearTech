# Generated by Django 4.2.16 on 2024-10-10 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0007_rename_tamanho_itemestoque_modelo'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tipo',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]