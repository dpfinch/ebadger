from django.db import models

# Create your models here.

class pub_info(models.Model):

    pub_name = models.CharField(max_length = 150)
    pub_lat = models.FloatField()
    pub_lon = models.FloatField()
    pub_street = models.CharField(max_length = 150)
    #  Need some attributes to the pub
    

    def __str__(self):
        return self.pub_name
