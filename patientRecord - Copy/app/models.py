from django.db import models

# Create your models here.
class Patient(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    mobile_no =models.CharField(max_length=50)
    address = models.TextField()
    detail = models.TextField()
    precout =models.TextField()
    visit_date =models.DateField(auto_now_add=True)
    next_visit_date = models.DateTimeField()
    
    def __str__(self):
        return self.full_name
    