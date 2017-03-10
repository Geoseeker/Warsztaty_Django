from django.db import models

TYPE = (
    (0,'domowy'),
    (1,'business'),
    (2,'private')
    )


class Person(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=64)
    description = models.TextField()
       

class Adress(models.Model):
    city = models.CharField(max_length=32)
    street = models.CharField(max_length=64)
    home_number = models.IntegerField()
    flat_number = models.IntegerField(default = True)
    adress = models.ForeignKey(Person) 


class Telephone(models.Model):
    number = models.ForeignKey(Person)
    tele_type = models.IntegerField(choices = TYPE)
    tele_number = models.IntegerField()

class Email(models.Model):
    email = models.ForeignKey(Person)
    email_type = models.IntegerField(choices = TYPE)
    email_address = models.EmailField(max_length=254)

# class Groups(models.Model):
#     group = models.ManyToManyField(Person)