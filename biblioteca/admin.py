from django.contrib import admin
from .models import Categoria, Editora, Livro

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone', 'email', 'site')
    search_fields = ('nome', 'email')

class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'editora', 'autor', 'ano_publicacao', 'editora', 'isbn', 'categoria')
    search_fields = ('titulo', 'autor', 'isbn')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Editora, EditoraAdmin)
admin.site.register(Livro, LivroAdmin)




# Register your models here.
