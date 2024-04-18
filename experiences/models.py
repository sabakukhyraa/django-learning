from django.db import models

# Create your models here.
class Experience(models.Model):
  companyName = models.CharField(max_length=100)
  jobTitle = models.CharField(max_length=100)
  startDate = models.DateTimeField(blank=True)
  endDate = models.DateTimeField(blank=True, null=True)
  description = models.TextField(blank=True)
  slug = models.SlugField(blank=True, unique=True)


  def __str__(self):
    return self.companyName