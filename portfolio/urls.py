from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # URLs de cursos
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),

    # URLs de autenticación
    path('signup/', views.signup, name='signup'),  # Cambié 'register' a 'signup'
    path('signin/', views.signin, name='signin'),  # Cambié 'login' a 'signin'
    path('signout/', views.signout, name='signout'),  # Cambié 'logout' a 'signout'

    # URLs de posts
    path('blog/', views.post_normal, name='posts'),
    path('blog/<int:post_id>/', views.detalle_post, name='detalle_post'),
]
