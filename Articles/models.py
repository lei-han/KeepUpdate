from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=500,blank=True)
    content_from  = models.CharField(max_length=30)
    creation_date = models.DateTimeField()
    content = models.FilePathField(blank=True,max_length=200)
    
    def __unicode__(self):
        return "[%s] %s" %(self.content_from, self.title) 
    
    #define more method here to do row ops in the table:
    #def newArticles(self,date):
    
