from django.db import models

# Create your models here.
class QuestionsFor10th(models.Model):
    # Q_id = models.AutoField()
    Q_name = models.CharField(max_length=3,default="q00")
    Question = models.CharField(max_length=300)
    op_1 = models.CharField(max_length=50)
    op_2 = models.CharField(max_length=50)
    op_3 = models.CharField(max_length=50)
    op_4 = models.CharField(max_length=50)
    correct_ans = models.CharField(max_length=1)
    # Q_Auto= models.AutoField()
    
    def __str__(self):
        return self.Question

from django.db import models

# ✅ 1️⃣ Category Model (Science, Commerce, Arts, etc.)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Category ka naam unique hoga

    def __str__(self):
        return self.name

# ✅ 2️⃣ Question Model (Each Question belongs to a Category)
class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Category ke saath link
    Question = models.TextField()  # Question text
    Q_name = models.CharField(max_length=100, unique=True)  # Unique question identifier
    op_1 = models.CharField(max_length=255)  # Option A
    op_2 = models.CharField(max_length=255)  # Option B
    op_3 = models.CharField(max_length=255)  # Option C
    op_4 = models.CharField(max_length=255)  # Option D
    correct_answer = models.CharField(max_length=1, choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')])  # Correct answer

    def __str__(self):
        return f"{self.category.name} - {self.Question[:50]}"
