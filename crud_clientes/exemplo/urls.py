from django.urls import path
from exemplo import views

app_name = 'exemplo'
urlpatterns = [
    path('', views.ClienteList.as_view(), name='list'),
    path('create/',views.CreateCliente.as_view(), name='create'),
    path('update/<int:pk>/',views.UpdateCliente.as_view(), name='update'),
    path('detail/<int:pk>/',views.DetailCliente.as_view(), name='detail'),
    path('delete/<int:pk>/',views.DeleteCliente.as_view(), name='delete'),
]