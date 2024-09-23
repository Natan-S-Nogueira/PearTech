from django.db import models

# Cliente
#     nome 
#     email
#     telefone
#     usuario

# Produto
#     imagem
#     nome
#     preco
#     ativo (BOOL)
#     categoria
#     tipo

# Categorias 
#     nome

# Tipos
#     nome

# ItemEstoque
#     produto
#     cor 
#     tamanho (modelo de celular)
#     quantidade

# IntensPedido
#     itemestoque
#     quantidade

# Pedido
#     cliente
#     data_finalizacao
#     finalizado
#     id_transacao
#     endereco
#     itenspedido

# Endereco
#     rua
#     numero
#     complemento
#     cep
#     cidade
#     estado
#     cliente