from django.db import models

# Create your models here.

class Luthier(models.Model):
    nome = models.CharField(max_length=120)
    cidade = models.CharField(max_length=100, blank=True)
    fundada_em = models.PositiveSmallIntegerField(null=True, blank=True)
    foto = models.ImageField(upload_to='luthiers/', blank=True, null=True)

    def __str__(self):
        return self.nome
 
class Guitar(models.Model):
    modelo = models.CharField(max_length=120)
    ano = models.PositiveSmallIntegerField(null=True, blank=True)
    descricao = models.TextField(blank=True)
    luthier = models.ForeignKey(Luthier, on_delete=models.CASCADE,
    related_name='guitarras')
    imagem = models.ImageField(upload_to='guitarras/', blank=True, null=True)
    
    def __str__(self):
        return "" + self.modelo + "-" + self.luthier.nome
