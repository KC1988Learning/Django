from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=100, unique=True)   # character field, with constraints, and unique identifier

    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    # on_detete: SET_NULL, even if reference objects are deleted, the referencing objects will be retained
    # for auditing purpose
    topic = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField(unique=True)  # unique field can apply for multiple attributes

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, null=True, on_delete=models.SET_NULL)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


