from django.db import models

# Create your models here.
class Experience(models.Model):
  companyName = models.CharField(max_length=100)
  jobTitle = models.CharField(max_length=100)
  startDate = models.DateTimeField()
  endDate = models.DateTimeField(blank=True, null=True)
  description = models.TextField()
  slug = models.SlugField(unique=True)