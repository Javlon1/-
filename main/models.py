from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    type = models.IntegerField(choices=(
        (1, 'admin'),
        (2, 'worker'),
        (3, 'client'),
    ), default=3)

    phone = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Info(models.Model):
    logo = models.ImageField(upload_to='logo/')
    email = models.EmailField()
    address = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    about = models.TextField()



class Slider(models.Model):
    img = models.ImageField(upload_to='slider/')
    title = models.CharField(max_length=255)
    text = models.TextField()


class We_Offer(models.Model):
    img = models.ImageField(upload_to='we offer/')
    title = models.CharField(max_length=255)
    text = models.TextField()


class Our_Areas(models.Model):
    img = models.ImageField(upload_to='our areas/')
    directions = models.CharField(max_length=255)
    text1 = models.TextField()
    text2 = models.TextField()


class Review(models.Model):
    subject = models.CharField(max_length=255)
    text = models.TextField()

class Our_Expertise(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='expertise/')


class Case_Study(models.Model):
    img = models.ImageField(upload_to='case study/')
    subject = models.CharField(max_length=255)
    text = models.TextField()
    data = models.DateField()


class Our_Team(models.Model):
    img = models.ImageField(upload_to='team/')
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    

class Blog(models.Model):
    img = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=255)
    data = models.DateField()
    text1 = models.TextField()
    text2 = models.TextField()


class About(models.Model):
    img = models.ImageField(upload_to='about/')
    text = models.TextField()



class About_Us_Detail(models.Model):
    img = models.ImageField(upload_to='about us detail/')
    text = models.TextField()
    data = models.DateField()


class Question(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(max_length=255)
    text = models.TextField()


class Map(models.Model):
    map = models.CharField(max_length=500)


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sms = models.CharField(max_length=500)
    data = models.DateTimeField(auto_now_add=True)


class Window(models.Model):
    sms = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

