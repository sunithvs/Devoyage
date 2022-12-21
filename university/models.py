from django.db import models


class Feedback(models.Model):
    user = models.ForeignKey('auth_login.User', on_delete=models.CASCADE)
    heading = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images')
    duration = models.IntegerField(default=0)
    intake = models.CharField(choices=(("fall", "fall"), ("spring", "spring"), ("summer", "summer")), max_length=100)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='course_images')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=100)
    images = models.ManyToManyField(Image)

    def __str__(self):
        return self.name


# create a model of University
class University(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    nirf_rank = models.IntegerField(default=-1)
    n_u_p = models.IntegerField(default=0, help_text="no of undergraduate programs")
    # TODO: make this array filed
    affiliations = models.CharField(max_length=100)
    # TODO: make this array field
    facilities = models.CharField(max_length=100)
    feedbacks = models.ManyToManyField(Feedback, related_name='feedbacks', blank=True, )
    courses = models.ManyToManyField(Course, related_name='courses', blank=True, )
    gallery = models.ManyToManyField(Gallery, related_name='gallery', blank=True, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Universities"
