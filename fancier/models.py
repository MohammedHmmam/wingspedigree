from django.db import models

class Fancier(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    #birthDate = models.DateField(auto_now = True , auto_now_add=False)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    region = models.CharField(max_length =30)
    street = models.CharField(max_length = 100)
    joinedDate = models.DateTimeField(auto_now_add=True)
    profilePicture = models.ImageField(default = 'defaultfancier.png' , blank = True)

    def __str__(self):
        return self.name