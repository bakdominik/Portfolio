from django.db import models


class Tag(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Project(models.Model):
    headline = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="static", default="images/placeholder.png")
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    live = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    
    def __str__(self):
        return self.headline