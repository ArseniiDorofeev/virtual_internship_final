# models.py

from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    fam = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    objects = models.Manager()

    def __str__(self):
        return f"{self.fam} {self.name} {self.otc}"


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return f"({self.latitude}, {self.longitude}, {self.height})"


class PerevalAdded(models.Model):
    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.TextField(blank=True, null=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    level_winter = models.CharField(max_length=10, blank=True, null=True)
    level_summer = models.CharField(max_length=10, blank=True, null=True)
    level_autumn = models.CharField(max_length=10, blank=True, null=True)
    level_spring = models.CharField(max_length=10, blank=True, null=True)

    STATUS_CHOICES = [
        ('new', 'New'),
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')

    objects = models.Manager()

    def __str__(self):
        return f"{self.beauty_title} {self.title}"


class PerevalImages(models.Model):
    data = models.TextField()
    title = models.CharField(max_length=255)
    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f"{self.title} ({self.pereval})"
