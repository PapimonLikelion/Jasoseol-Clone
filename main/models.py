from django.db import models
from django.contrib.auth.admin import User
# Create your models here.


class Jasoseol(models.Model):
    SI = (
        ("seoul", "seoul"),
        ("daegu", "daegu"),
    )

    GU = (
        ("seoul", (
            ("seodaemoon", "seodaemoon"),
            ("mapo", "mapo"),    
        )),
        ("daegu", (
            ("bukgu", "bukgu"),
            ("suseong", "suseong"),
        )),
    )

    title = models.CharField(max_length=50)
    content = models.TextField()
    location_si = models.CharField(
        max_length=20,
        choices=SI,
        default='1'
    )
    location_gu = models.CharField(
        max_length=20,
        choices=GU,
        default='1'
    )
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    jasoseol = models.ForeignKey(Jasoseol, on_delete=models.CASCADE)

    def __str__(self):
       return self.author