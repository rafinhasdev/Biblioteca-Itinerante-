from django.db import models
from accounts.models import CustomUser


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Editora(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    site = models.URLField()

    def __str__(self):
        return self.nome
    

class Livro(models.Model):
    titulo = models.CharField(max_length=100, null=True)
    descricao = models.TextField()
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, null=True)
    autor = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    editora = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    capa = models.ImageField(upload_to='livros/', blank=True)


    def __str__(self):
        return f"{self.titulo}, de: {self.autor}"


