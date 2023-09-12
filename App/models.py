from django.db import models

# Create your models here.


class Record(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField(null=True)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
# class Post(models.Model):
#     contenet=models.TextField()
#     # image=models.ImageField()
#     title=models.CharField(max_length=200)
#     posted_at=models.DateTimeField(auto_now=True)