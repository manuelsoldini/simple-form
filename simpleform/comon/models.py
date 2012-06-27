from django.db import models


class SimpleForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mail = models.EmailField()
    phone = models.CharField(max_length=20)
    linkToLinkedin = models.URLField(none=True)
    resume = models.FileField(upload_to='resumes', none=True)
    date = models.DateTimeField(auto_now=True)

