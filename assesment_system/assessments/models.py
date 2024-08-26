from django.db import models

# Create your models here.
class Assessment(models.Model):
    title = models.CharField(max_length=255)
    assessment_type = models.CharField(max_length=50)  # e.g., quiz, assignment, survey
    instructions = models.TextField()
    time_limit = models.IntegerField()  # time limit in minutes
    attempts_allowed = models.IntegerField()
    feedback_options = models.TextField()  # description of feedback options

    def __str__(self):
        return self.title