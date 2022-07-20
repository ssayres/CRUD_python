from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_created=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Project2(True):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Project2'
        verbose_name_plural = 'Projects2'

    def __str__(self):
        return self.titulo


class Avaliacao(Base):
    project2 = models.ForeignKey(Project2, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliacao'
        verbose_name_plural = 'Avaliacoes'
        unique_together = ['email', 'project2']

        def __str__(self):
            return f'{self.nome} avaliou o curso {self.project2} com a nota {self.avaliacao}'
