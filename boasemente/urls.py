
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livro/', include('livro.urls')),
    path('auth/',include('usuario.urls'))
]

# definir uma rota para aplicação, fluxo de navegação