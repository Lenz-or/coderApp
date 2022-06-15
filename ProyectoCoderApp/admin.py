from django.contrib import admin

from ProyectoCoderApp.models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display= ('nombre', 'comision')


admin.site.register(Curso, CursoAdmin)

# Register your models here.

# admin, admin -> python manage.py createsuperuser
