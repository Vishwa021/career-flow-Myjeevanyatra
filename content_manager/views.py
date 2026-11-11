from django.contrib.auth.models import User, auth
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from Users.models import Blog
from Career.models import Career
from django.contrib.auth.models import User
from .models import Register

def index(request):
    careers = Career.objects.all()
    blog = Blog.objects.filter(status='approved').order_by('-Created_Date')
    user = request.user
    user_count = User.objects.count()
    career_count = Career.objects.count()
    
    context = {"careers": careers, "blog": blog, "user": user , "user_count": user_count, "career_count": career_count}
    return render(request, "newindex.html", context)

def logout_user(request):
    auth.logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('index')

def login_views(request):  # Rename function to avoid conflict
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)  # Correct authentication

        if user is not None:
            auth.login(request, user)  # Log the user in properly
            messages.success(request, "Login successful!")
            
             # Fetch rejected and approved blogs
            rejected_blogs = Blog.objects.filter(author=user, status="rejected")
            approved_blogs = Blog.objects.filter(author=user, status="approved")

            # Show rejection message & delete rejected blogs
            if rejected_blogs.exists():
                messages.info(request, "Your blog was rejected and has been deleted.")
                rejected_blogs.delete()  # Delete rejected blogs immediately

            # Show approval message
            elif approved_blogs.exists():
                messages.success(request, "Congratulations! Your blog was approved.")
                
            # return render(request, 'newindex.html')
            return redirect('index')
        else:
            messages.info(request, "Invalid username or password.")  # Generic error message
            return redirect('login')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fullname = request.POST['fullname']
        phone = request.POST['phone']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        gender = request.POST['gender']
        try:
            first_name = fullname.split()[0]
            last_name = fullname.split()[1]
            
        except IndexError:
            messages.info(request, 'Please enter your full name')
            return redirect('registeration')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')            
            else:
                user = User.objects.create_user(
                    username=username, first_name=first_name,
                    last_name=last_name, email=email, password=password1
                )
                user.save()
            
                register = Register(
                    fullname=fullname, 
                    phone=phone, gender=gender
                )
                register.save()    
                messages.success(request, 'User created')
            
            
                return render(request, 'login.html')
            

                
                # send_mail(
                #     subject="Welcome to CineVerse!",
                #     message=f"Hi {first_name},\n\nWelcome to CineVerse!\n\nUsername: {username}\nPassword: {password1}\n\nEnjoy booking your favorite movie shows with CineVerse!",
                #     from_email=settings.EMAIL_HOST_USER,
                #     recipient_list=[email],
                #     fail_silently=False,
                # )

                # messages.info(request, 'User created')
                # return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
        return redirect('registeration')
    else:
        return render(request, "registeration.html")

