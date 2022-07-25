from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from exemplo.models import Cliente

class ClienteList(ListView):
    model = Cliente
    queryset = Cliente.objects.all()

class CreateCliente(CreateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('exemplo:list')

class UpdateCliente(UpdateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('exemplo:list')

class DetailCliente(DetailView):
    queryset = Cliente.objects.all()

class DeleteCliente(DeleteView):
    queryset = Cliente.objects.all()
    success_url = reverse_lazy('exemplo:list')

