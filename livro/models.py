from django.db import models
from datetime import date
# ORM: uma forma de trabalhar com POO através de banco de dados. Ou seja, as classes do seu projeto serão como tabelas no seu banco de dados. 
# variáveis de classe: colunas do banco de dados

# class Emprestimo(models.Model):
# null <> blank 
# blank: string vazia
# null : deixa receber o valor null

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=30, blank= True)
    data_cadastro = models.DateField(default=date.today)
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=30, blank= True,null=True)
    data_emprestimo = models.DateTimeField( blank= True, null=True)
    data_devolucao = models.DateField(blank= True, null=True)
    tempo_duracao = models.DateField(blank= True, null=True)

    def __str__(self):
        return self.nome
    

