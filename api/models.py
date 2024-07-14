from django.db import models

class CalendarEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    email1 = models.EmailField()
    email2 = models.EmailField()

    def __str__(self):
        return self.title