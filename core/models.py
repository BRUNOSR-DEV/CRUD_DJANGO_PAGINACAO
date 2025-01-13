from django.db import models

class Produto(models.Model):     
    '''Tabela Produto, herdando de models.Model do django'''

    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome
