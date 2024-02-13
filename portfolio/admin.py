from django.contrib import admin

# Register your models here.

from .views import *

admin.site.register(About)
admin.site.register(Competence)
admin.site.register(Projet)
admin.site.register(Client)
