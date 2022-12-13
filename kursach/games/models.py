from django.db import models

class games(models.Model):
    ID_GAme= models.CharField(max_length=5,)
    Name_of_Game = models.CharField(max_length=128,)
    Description = models.TextField()
    Teg = models.CharField(max_length=3,)
    def __str__(self):
        return ' '.join([self.ID_GAme,self.Name_of_Game,self.Description,self.Teg])



