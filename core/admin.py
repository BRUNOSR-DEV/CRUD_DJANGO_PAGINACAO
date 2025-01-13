from django.contrib import admin

from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    ''' Representação da tabela Produto na administração do django'''
    list_display = ('nome', 'preco')
