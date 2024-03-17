from django.contrib import admin

from usuarios.models import Persona, Alumno

# Register your models here.
# admin.site.register(Post) #Aqui hay quye registar todos nuetsros modelos para que django pueda encontrarlos
@admin.register(Persona)  # ESta es la forma moderna de registar modelos
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'edad', 'correo', 'telefono']  # Define qué campos del modelo Persona se mostrarán en la lista de elementos del panel de administración
    list_filter = ['nombre', 'apellido']  # Agregar filtros en el panel de administracion
    search_fields = ['nombre', 'apellido']  # Define los campos que se utilizan para la busqueda

    ordering = ['nombre', 'apellido']  # define el orden en el que se mostrarán los elementos en el panel de administración


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['num_boleta', 'carrera', 'plan']
    list_filter = ['num_boleta', 'carrera', 'plan']
    search_fields = ['num_boleta', 'carrera', 'plan']
