# Generated by Django 5.1.1 on 2024-09-24 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loja", "0003_alter_cliente_nome_alter_produto_imagem"),
    ]

    operations = [
        migrations.CreateModel(
            name="Banner",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("imagem", models.ImageField(blank=True, null=True, upload_to="")),
                (
                    "link_destino",
                    models.CharField(blank=True, max_length=400, null=True),
                ),
                ("ativo", models.BooleanField(default=False)),
            ],
        ),
    ]
