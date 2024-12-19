from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Villa(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    emplacement = models.CharField(max_length=200)
    lien_visite = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="villas/", blank=True, null=True)

    def __str__(self):
        return self.nom




class Visit(models.Model):
    villa = models.ForeignKey(Villa, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=50, choices=[('visit', 'Visite'), ('purchase', 'Achat')])

    def __str__(self):
        return f"{self.villa.nom} ({self.action})"
