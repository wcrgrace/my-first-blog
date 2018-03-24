from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model): #create an object
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE) #link to another model
    title = models.CharField(max_length = 200) # define limited length
    text = models.TextField() #unlimited length
    create_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self): #method with the name "publish"
        self.published_date = timezone.now()
        self.save()

    def _str_(self):
        return self.title #returns a post title
