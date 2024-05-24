from django.db import models

class GeneralSetting(models.Model):

  generalSettingTitle = models.CharField(null=True, max_length=100)
  content = models.TextField(null=True, default='Unknown')

  def __str__(self):
    return self.generalSettingTitle
