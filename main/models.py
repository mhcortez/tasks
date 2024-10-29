from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11) 
    
    def __str__(self):
        return self.nome