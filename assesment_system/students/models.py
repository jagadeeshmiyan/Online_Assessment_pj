from django.db import models

# Create your models here.
from assessments.models import Assessment

class StudentResponse(models.Model):
    assessment = models.ForeignKey(Assessment, related_name='responses', on_delete=models.CASCADE)
    student_id = models.IntegerField()
    responses = models.JSONField()  # Store responses as a JSON object

    def __str__(self):
        return f"Response for assessment {self.assessment.title} by student {self.student_id}"