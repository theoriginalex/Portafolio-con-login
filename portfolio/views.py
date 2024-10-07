from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Project, Post, Curso
from django.db import IntegrityError
from django.contrib.auth.models import User

#PORTAFOLIOS
# Página de inicio
def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

#----------------------------------------------------------------
#BLOGS
# Lista de posts
@login_required(login_url='home')
def post_normal(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

# Detalle de un post
@login_required(login_url='home')
def detalle_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

#----------------------------------------------------------------
#EXPERIENCIA
# Lista de cursos
@login_required(login_url='home')
def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'curso/curso_list.html', {'cursos': cursos})

# Detalle de un curso
@login_required(login_url='home')
def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    return render(request, 'curso/curso_detail.html', {'curso': curso})

#----------------------------------------------------------------
#INICIAR SESION Y CERRAR SECION
# Registro de usuario
def signup(request):
    if request.method == 'GET':
        return render(request, 'registration/signup.html', {"form": UserCreationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'registration/signup.html', {"form": UserCreationForm(), "error": "El nombre de usuario ya existe."})
        return render(request, 'registration/signup.html', {"form": UserCreationForm(), "error": "Las contraseñas no coinciden."})

# Iniciar sesión
def signin(request):
    if request.method == 'GET':
        return render(request, 'registration/signin.html', {"form": AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'registration/signin.html', {"form": AuthenticationForm(), "error": "Usuario o contraseña incorrectos."})
        login(request, user)
        return redirect('home')

# Cerrar sesión
@login_required(login_url='home')
def signout(request):
    logout(request)
    return redirect('home')

