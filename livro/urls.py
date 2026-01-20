from django.urls import path 
# do arquivo tal importe a função tal
from . import views 
# o ponto ( . ) referencia a propria pasta que o arquivo está, nesse caso a pasta livro
# vai receber uma request e retornar uma response 


# função path do django: nos permite criar rotas (em forma de lista)
# django utiliza o padrao MVT :
# model: o arquivo responsavel pela manipulação do BD (armazena a info)
# view: lógica do projeto (if, else, for -> tratamento de dados)
# template: parte visual do projeto, o que será apresentado na tela

urlpatterns = [  
    path('cadastrar/', views.cadastrar)
]