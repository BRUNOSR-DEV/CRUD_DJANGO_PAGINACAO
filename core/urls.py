from django.urls import path

from django.contrib import admin

from .views import IndexView, CreateProdutoView, UpdateProdutoView, DeleteProdutoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add', CreateProdutoView.as_view(), name='add_produto'),
    path('<int:pk>/update/', UpdateProdutoView.as_view(), name='upd_produto'),
    path('<int:pk>/delete/', DeleteProdutoView.as_view(), name='del_produto'),
]

admin.AdminSite.site_header = 'Sistema Brunão'
admin.AdminSite.site_tittle = 'Brunão do Curso'
admin.AdminSite.index_titte = 'Meu sistema Brunão'