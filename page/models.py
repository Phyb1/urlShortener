from django.db import models

# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length=250)
    info = models.DateTimeField(auto_now_add=True)
    import random
    key = int(100000*random.random())
    keys = models.IntegerField(default=key)
    short = models.CharField(max_length=50, default='http://127.0.0.1:8000/'+str(key)+'/')

    class Meta:
        verbose_name = ("link url")
        verbose_name_plural = ("links")

    def __str__(self):
        return self.name


 