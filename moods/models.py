from django.db import models

class Mood(models.Model):
	MOODSWING_CHOICES = [
        (-2, 'Very Hard'),
        (-1, 'Hard'),
        (0, 'Normal'),
        (1, 'Good'),
        (2, 'Very Good'),
    ]
	moodswing = models.IntegerField(choices=MOODSWING_CHOICES)
	created_at = models.DateTimeField(auto_now_add =True)