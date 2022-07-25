from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nome


