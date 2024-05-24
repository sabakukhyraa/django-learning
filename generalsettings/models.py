from django.db import models

class GeneralSetting(models.Model):

  content = models.TextField(null=True, default='Unknown')

  def __str__(self):
    return self.content
