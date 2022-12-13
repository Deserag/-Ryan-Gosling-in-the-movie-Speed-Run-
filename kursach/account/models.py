from django.db import models
class account(models.Model):
    Decription = models.CharField(max_length=  10000,)
    Price = models.IntegerField()
    ID_Game = models.CharField(max_length= 100,)
    def __str__(self):
        return ' '.join([self.Decription,self.Price, self.ID_Game])
