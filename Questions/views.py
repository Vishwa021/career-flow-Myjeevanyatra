import random
import json
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Question, Category  # Models import karo

# ✅ 1️⃣ Test Start View (Random Questions Fetch)
def test_view(request):
    categories = Category.objects.all()  # Jitni categories hain unko fetch karlo
    questions = {}  

    for category in categories:
        category_questions = list(Question.objects.filter(category=category))
        questions[category.name] = random.sample(category_questions, min(10, len(category_questions)))

    return render(request, 'test.html', {'questions': questions})

# ✅ 2️⃣ Test Submit View (User ke Answers Validate karna)
def submit_test(request):
    if request.method == 'POST':
        categories = Category.objects.all()
        scores = {category.name: 0 for category in categories}  # Category-wise score tracking
        
        for category in categories:
            questions = Question.objects.filter(category=category)
            for question in questions:
                user_answer = request.POST.get(question.Q_name)
                if user_answer == question.correct_answer:  # Agar answer sahi hai to score badhao
                    scores[category.name] += 1
        
        query_params = '&'.join([f'{key}={value}' for key, value in scores.items()])
        
        return redirect(f"{reverse('questions:result')}?{query_params}")  # Result page pe bhejo

# ✅ 3️⃣ Result View (Graph ke liye Data Process Karna)
def result(request):
    science_score = request.GET.get('Science', 0)  
    commerce_score = request.GET.get('Commerce', 0)
    arts_score = request.GET.get('Arts', 0)

    scores = {
        'Science': int(science_score),
        'Commerce': int(commerce_score),
        'Arts': int(arts_score),
    }
    max_score = 10
    return render(request, 'result.html', {
        'categories_json': json.dumps(list(scores.keys())),  # Convert keys to JSON
        'scores_json': json.dumps(list(scores.values())),    # Convert values to JSON
        'max_score': max_score
    })