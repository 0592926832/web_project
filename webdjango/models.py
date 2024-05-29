from django.db import models

class MyModel(models.Model):
    username = models.CharField (max_length=100)
    email_address = models.EmailField (max_length=254)
    #id = models.AutoField(primary_key=True)
    password = models.CharField (max_length=100)
    
    class meta:
        db_table="register"
    
   # def __str__(self):
     #   return self.usernamed