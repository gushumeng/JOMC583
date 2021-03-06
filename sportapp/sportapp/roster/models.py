from django.db import models

# Create your models here.

class Player(models.Model):
    no = models.IntegerField(unique= True, max_length=3)
    name = models.CharField(max_length=20)
    position = models.CharField(unique=False, max_length=10)
    height = models.CharField(unique=False, max_length=10)
    year = models.CharField(max_length=5)
    hometown = models.TextField()
    highSchool = models.TextField()
    club = models.TextField()
    juniorSeason = models.TextField(null=True)
    sophomoreSeason = models.TextField(null=True)
    freshmanSeason = models.TextField(null=True) 
    image = models.TextField()

    class Meta(object):
	ordering = ('no', 'name')

    def __unicode__(self):
	return U'%d %s' %(self.no, self.name)
    
    
        
    
