from django.db import models

categorylist = [
    ("shirt", "shirt"),
    ("tshirt", "tshirt"),
    ("jeans", "jeans"),
    ("short", "short"),
    ("shoes", "shoes"),
    ("hoodie", "hoodie"),
    ("accessories", "accessories"),
]


class user(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.TextField()
    address = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)


class product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(choices=categorylist, max_length=50)
    desc = models.TextField(blank=True, null=True)
    istrend = models.BooleanField(default=False)
    price = models.CharField(max_length=10)
    cover = models.URLField()
    img2 = models.URLField(null=True, blank=True)
    img3 = models.URLField(null=True, blank=True)
    img4 = models.URLField(null=True, blank=True)
    img5 = models.URLField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name