from django.db import models


class Username(models.Model):

    username = models.TextField(null = True, blank=True)
    
    def __str__(self):
        return self.username


class Review(models.Model):

    review = models.TextField(null=True, blank=True)
    review_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.review