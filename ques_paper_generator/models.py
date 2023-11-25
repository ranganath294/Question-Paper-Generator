from django.db import models



class Questions(models.Model):
    
    DIFFICULTY = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )
    
    question = models.TextField()
    subject = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY)
    marks = models.IntegerField()
    