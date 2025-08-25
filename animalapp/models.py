from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=200)
    sound = models.CharField(max_length=50)

    def speak(self):
        return f'The {self.name} says "{self.sound}"'
