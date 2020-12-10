from django.db import models
from fancier.models import Fancier

class Pigeon(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=15)
    sex = models.CharField(max_length=1)
    birthYear = models.CharField(max_length=6)
    ringNumber = models.CharField(max_length=20)
    #father = models.CharField(max_length=20)
    #mother = models.CharField(max_length=20)
    #manager = models.ForeignKey('self', null=True, related_name='employee')
    father = models.ForeignKey('self' , null=True , related_name='pigeonFather', on_delete = models.PROTECT)
    mother = models.ForeignKey('self' , null=True , related_name='pigeonMother' , on_delete=models.PROTECT)
    fancier = models.ForeignKey(Fancier , default=None , on_delete = models.PROTECT)
    thumb = models.ImageField(default = 'defaultpigeon.jpg', blank = True)

    def __str__(self):
        return self.name

