from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name
    

class Jobseeker(models.Model):
    name = models.CharField(max_length=50, blank=False)
    id_number = models.IntegerField(blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    profession = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to='uploads/jobseekers/')

    def __str__(self):
        return f"{self.name}, {self.profession}, {self.location}"


class Job(models.Model):
    title = models.CharField(max_length=50, blank=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    pay = models.DecimalField(max_digits=6, decimal_places=2)
    completed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='uploads/jobs/')

    def __str__(self):
        return f"{self.title}, R{self.pay}, {self.location}"
    

class Vendor(models.Model):
    name = models.CharField(max_length=50, blank=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    product = models.CharField(max_length=20, blank=False)
    image = models.ImageField(upload_to='uploads/vendors/')

    def __str__(self):
        return f"{self.name}, {self.location}"


class Product(models.Model):
    product_name = models.CharField(max_length=50, blank=False)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return f"{self.product_name}, {self.product_price}"


class Client(models.Model):
    name = models.CharField(max_length=50, blank=False)
    id_number = models.IntegerField(blank=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, default='')
    image = models.ImageField(upload_to='uploads/client/')

    def __str__(self):
        return f"{self.name}, {self.location}"
