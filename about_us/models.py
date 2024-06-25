from django.db import models


class Username(models.Model):

    username = models.TextField(null = True, blank=True)
    
    def __str__(self):
        return self.username


class Review(models.Model):

    username = models.ForeignKey('Username', null=True, blank=True, on_delete=models.SET_NULL)
    review = models.TextField(null=True, blank=True)
    review_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.review