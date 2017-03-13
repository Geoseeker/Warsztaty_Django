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
    
    def __str__(self):
        return"Name:{} Surname:{} Description:{}".format(self.name, self.surname, self.description)
       

class Adress(models.Model):
    city = models.CharField(max_length=32)
    street = models.CharField(max_length=64)
    home_number = models.IntegerField()
    flat_number = models.IntegerField(null = True, blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE) 


class Telephone(models.Model):
    tele_type = models.IntegerField(choices = TYPE)
    tele_number = models.IntegerField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

class Email(models.Model):
    email_type = models.IntegerField(choices = TYPE)
    email_address = models.EmailField(max_length=254)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

# class Groups(models.Model):
#     group = models.ManyToManyField(Person)