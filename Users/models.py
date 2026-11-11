from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.template.defaultfilters import slugify

# Create your models here.
#blog model
class Blog(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='static/img/blog/', default='static/img/blog.webp',null=True, blank=True)
    content = models.TextField(help_text="Write your blog content here")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    Created_Date = models.DateField(default=date.today)
    slug = models.CharField(max_length=1000,null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + "-" +str(self.Created_Date))
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title + " | " + str(self.author)
#blog comment model
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(help_text="Write your comment here")
    Created_Date = models.DateField(default=date.today)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"

