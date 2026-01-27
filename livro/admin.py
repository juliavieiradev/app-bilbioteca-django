from django.contrib import admin
from .models import Livro
# da pasta que eu estou, importe do arquivo models a classe Livro
# @: decorador, consome outra função e modifica essa função (personalizar área administrativa)

admin.site.register(Livro)

