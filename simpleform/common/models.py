from django.db import models
import os, datetime

def upload_to_path(instance, filename):
    base = "resumes"
    name = instance.first_name
    name += '-' + instance.last_name
    name += '_' + datetime.datetime.now().strftime('%S%f')
    name += '.' + filename.split('.')[-1]
    return os.path.join(base, name)


class SimpleForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mail = models.EmailField()
    phone = models.CharField(max_length=20)
    link_to_linkedin = models.URLField(null=True, blank=True)
    resume = models.FileField(upload_to=upload_to_path, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

