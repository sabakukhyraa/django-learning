from django.db import models

class Project(models.Model):

  projectName = models.CharField(null=True, max_length=100)
  # projectImage = models.ImageField()
  description = models.TextField(null=True, default='Unknown')

  def __str__(self):
    return self.projectName
