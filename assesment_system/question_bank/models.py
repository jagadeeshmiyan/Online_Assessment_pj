from django.db import models

# Create your models here.
from assessments.models import Assessment

class Question(models.Model):
    assessment = models.ForeignKey(Assessment, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    question_type = models.CharField(max_length=50)  # e.g., multiple-choice, short answer
    options = models.JSONField(blank=True, null=True)  # only for multiple-choice

    def __str__(self):
        return self.question_text