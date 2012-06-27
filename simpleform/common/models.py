from django.db import models


class SimpleForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mail = models.EmailField()
    phone = models.CharField(max_length=20)
    link_to_linkedin = models.URLField(null=True, blank=True)
    resume = models.FileField(upload_to='resumes', null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

