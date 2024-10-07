from django.contrib import admin

# Register your models here.
from .models import Project,  Post, Curso

admin.site.register(Project)
admin.site.register(Post)
admin.site.register(Curso)