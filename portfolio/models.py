from django.db import models



# Modèle momba ny about
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")
    
    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"
   
# Modèle momba ny compétence 
class Competence(models.Model):
    name = models.CharField(max_length=100, verbose_name="Competence name")
    description = models.TextField(verbose_name="About competence")
    
    def __str__(self):
        return self.name
# Modèle momba ny projet    
class Projet(models.Model):
    title = models.CharField(max_length=100, verbose_name="Projet title")
    image = models.ImageField(upload_to="projets")
    
    def __str__(self):
        return self.title
    
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Client name")
    description = models.TextField(verbose_name="Client say")
    image = models.ImageField(upload_to="clients", default="default.png")
    
    def __str__(self):
        return self.name