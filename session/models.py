from django.db import models


# Create your models here.

# Models of different Topics
class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='video_set')

    def __str__(self):
        return self.name


#  model of multiple choice questions
class MCQ(models.Model):
    question = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='mcq_set')

    def __str__(self):
        return self.question
