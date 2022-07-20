from django.contrib import admin

# Register your models here.

from .models import Project2, Avaliacao


@admin.register(Project2)
class Project2Admin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'criacao', 'atualizacao', 'ativo')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('project2', 'nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo')