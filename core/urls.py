from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from biblioteca import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listar_livros, name='listar_livros'),
    path('livro/adicionar_livro/', views.adicionar_livro, name='adicionar_livro'),
    path('livro/editar_livro/<int:pk>/', views.editar_livro, name='editar_livro'),
    path('livro/deletar_livro/<int:pk>/', views.deletar_vaga, name='deletar_livro'),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


