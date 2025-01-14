from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Produto
from .forms import ProdutoModelForm

class IndexView(ListView):
    models = Produto #listar produtos
    template_name = 'index.html' #pagina index
    paginate_by = 5
    ordering = 'id'
    queryset = Produto.objects.all() #trazendo todos os produtos
    #context_object_name = 'produtos' #dando um nome a tabela, passado no template html

class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto_criacao.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('add_produto')


class UpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')


class DeleteProdutoView(DeleteView):
    model = Produto
    template_name = 'produto_del.html'
    success_url = reverse_lazy('index')
