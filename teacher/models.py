from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    image_profile = models.ImageField(upload_to='teacher_profiles/')
    video = models.FileField(upload_to='teacher_videos/')

    def __str__(self):
        return self.name