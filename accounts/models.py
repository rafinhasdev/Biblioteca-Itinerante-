from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    
    Cargos = [
        'Cliente',
        'Autor',
        'Editor',
    ]

    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    cargo = models.CharField(max_length=20, choices=[(cargo, cargo) for cargo in Cargos])
    foto_perfil = models.ImageField(upload_to='perfil/', blank=True, null=True, verbose_name='Foto de Perfil')

    def __str__(self):
        return self.nome
    
    def is_cliente(self):
        return self.groups.filter(name='Cliente').exists()
    
    def is_autor(self):
        return self.groups.filter(name='Autor').exists()
    
    def is_editor(self):
        return self.groups.filter(name='Editor').exists()
    
    def is_administrador(self):
        return self.groups.filter(name='Administrador').exists()
    




# Create your models here.
