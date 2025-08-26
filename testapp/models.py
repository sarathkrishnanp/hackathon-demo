from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)  # store hashed in real projects

    def __str__(self):
        return self.name

# Hostel
class Hostel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    rooms = models.IntegerField()
    rent_per_month = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Booking
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.name} → {self.hostel.name}"