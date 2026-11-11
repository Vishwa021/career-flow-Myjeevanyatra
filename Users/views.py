from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import Blog, Comment
from django.contrib import messages

# Create your views here.
def blog(request,slug):
    blogs = get_object_or_404(Blog,slug=slug)
    comments = Comment.objects.filter(blog=blogs).order_by('-Created_Date')
    context = {'blogs': blogs, 'comments': comments}
    return render(request, "blog.html", context)

# Ensures only logged-in users can comment
def add_comment(request, slug):
    if request.method == "POST":
        comment_text = request.POST.get("content")  # Get comment text from form

        # Fetch the blog using slug
        blog = get_object_or_404(Blog, slug=slug)

        # Create the comment
        Comment.objects.create(
            user=request.user,  # Get the logged-in user
            comment=comment_text,
            blog=blog  # Link the comment to the correct blog
        )
        
        messages.success(request, "Comment added successfully!")

        # Redirect back to the same blog page after commenting
        return redirect("blog", slug=blog.slug)

def write_blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")  # Get the uploaded image

        if not title or not content:
            messages.error(request, "Title and Content cannot be empty.")
            return render(request, "write_blog.html")

        # Save the blog as pending for admin approval
        blog = Blog.objects.create(
            title=title,
            content=content,
            image=image,
            author=request.user,  # Assuming user is logged in
            status="pending"  # Mark as pending for approval
        )

        messages.success(request, "Your blog has been submitted for review!")
        return redirect("index")  # Redirect to home page after submission

    return render(request, "write_blog.html")