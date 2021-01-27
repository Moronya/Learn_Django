from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=30, unique = True, help_text="A label for URL config. ")

    def __str__(self):
        return self.name.title()
    
    class Meta:
        ordering = ['name']

class Startup(models.Model):
    name = models.CharField(max_length=60,db_index = True)
    slug = models.SlugField(max_length=30, unique = True,       help_text="A label for URL config. ")
    description = models.CharField(max_length=70)
    founded_date = models.DateField("Date founded")
    contact = models.EmailField()
    website = models.URLField(max_length = 255) 
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date' #ensure that the latest startup should be the object with the most recent founded_date
    
class NewsLink(models.Model):
    title = models.CharField(max_length=60)
    pub_date = models.DateField('date published')
    link = models.URLField()
    startup = models.ForeignKey(Startup, on_delete = models.CASCADE)

    def __str__(self):
        return "{}:{}".format(self.Startup, self.title)
    
    class Meta:
        verbose_name = 'news article'
        ordering = ['-pub_date'] #the dash switches the ordering from ascending to descending. The items are ordered from newest to the oldest
        get_latest_by = 'pub_date'


