
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include
from portfolio import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')), # mampiditra ny url an'ilay application
    path('signup/', views.inscriptionView,name="inscription"),
    path('login/',views.ConnexionView,name='connexion'),
    path('contact/', views.contactView, name='contact')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
