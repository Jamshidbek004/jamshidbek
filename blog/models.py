from django.contrib.auth.models import User
from django.db import models
from django.db import models
from django.utils import timezone

from django.urls import reverse
# Create your models here.
class Category(models.Model):
    nomi = models.CharField(max_length=250)
    def __str__(self):
        return self.nomi

class News(models.Model):
    class Status(models.TextChoices):
        qoralama = "QR","qoralama"
        chopetilish = "CHP", "chopetilish"

    nom = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=250)
    kontent = models.TextField()
    rasm = models.ImageField(upload_to='news/images')
    filelar = models.FileField(upload_to='news/fayllar')
    chopetilishVaqti = models.DateTimeField(default=timezone.now)
    yaratilganVaqti =models.DateTimeField(auto_now_add=True)
    ozgarishVaqti = models.DateTimeField(auto_now=True)
    holati =models.CharField(max_length=3,choices=Status.choices,default=Status.qoralama)

    kategory = models.ForeignKey(Category,on_delete=models.CASCADE)
    korishlarsoni = models.IntegerField(default=0)
    comentlarsoni = models.IntegerField()
    qaynoq_yangiliklar = models.BooleanField(default=False)

    class Meta:
        ordering = ['-chopetilishVaqti']
    objects = models.Manager()

    def __str__(self):
        return self.nom
    def get_absolute_url(self):
        return reverse("news_detail",args=[self.slug])

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=500)
    message = models.TextField()
    subject = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("list")


class Email(models.Model):
    email = models.CharField(max_length=222)


class Comment(models.Model):
    news = models.ForeignKey(News,
                            on_delete=models.CASCADE,
                             related_name='comments')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='comments')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    avtive = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_time']
    def __str__(self):
        return f"Comment - {self.body} by {self.user}"

class reklama(models.Model):
    rasm = models.ImageField(upload_to='news/images')
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

class Magazin(models.Model):
    rasm = models.ImageField(upload_to='news/images')
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
class Follow_us(models.Model):
    foydalanuvchilar = models.IntegerField()
    nomi = models.CharField(max_length=100)

    def __str__(self):
        return self.nomi

class Get_in_touch(models.Model):
    tel_raqam = models.IntegerField()
    lakatsiya = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class Telfon(models.Model):

    name = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(max_length=100)

    def get_absolute_url(self):
        return reverse("news_detail_page",args=[self.slug])
    def __str__(self):
        return self.name

