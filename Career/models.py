from django.db import models
from datetime import date
from django.template.defaultfilters import slugify
# Create your models here.
class Career(models.Model):
    image = models.ImageField(upload_to='static/img/career/', default='static/img/career.webp',null=True)
    title = models.CharField(max_length=100)
    What_is_it_about = models.TextField(help_text="Write what is your career is about")
    Inspiration_to_start = models.JSONField(help_text="Write what inspired you to start this career")
    famous_person = models.JSONField(help_text="Write about famous person in this career")
    learn_more = models.JSONField(help_text="Write more about this career")
    Essential_skills = models.JSONField(help_text="Write about essential skills in this career")
    Career_Oppertunities = models.JSONField(help_text="Write about career oppertunities in this career")
    Created_Date = models.DateField(default=date.today)
    slug = models.CharField(max_length=1000,null=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + "-" +str(self.Created_Date))
        return super().save(*args, **kwargs)    