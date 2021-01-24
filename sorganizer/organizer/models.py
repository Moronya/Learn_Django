from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=30, unique = True, help_text="A label for URL config. ")
    def __str__(self):
        return self.name

class Startup(models.Model):
    name = models.CharField(max_length=60,db_index = True, help_text= 'A label for URL config. ') #when the db_index parameter is set to True, the values are automatically indexed in the database 
    founded_date = models.DateField("Date founded")
    contact = models.EmailField()
    website = models.URLField(max_length = 255) 
    tags = models.ManyToManyField(Tag)
    
class NewsLink(models.Model):
    title = models.CharField(max_length=60)
    pub_date = models.DateField('date published')
    link = models.URLField()
    startup = models.ForeignKey(Startup)

    def __str__(self):
        return *{}:{}*.format(self.Startup, self.title)


