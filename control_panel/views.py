from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.contrib.auth import logout
from django.contrib.auth.models import User
from control_panel.models import Book
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import UserForm
from django.views import View
from .forms import ContentForm
from .models import Content
from .forms import BookForm  
from .models import Settings  # Assuming Settings is a model to store site settings
from .forms import SettingsForm



def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        
        user = authenticate(request, username=username, password=password)
        
        
        if user is not None:
            if user.is_staff:
                
                login(request, user)
                return redirect('admin_dashboard')  
            else:
                
                messages.error(request, "You are not authorized to access the admin panel.")
                return render(request, 'control_panel/admin_login.html')  
        else:
            
            messages.error(request, "Invalid username or password.")
            return render(request, 'control_panel/admin_login.html')  

    return render(request, 'control_panel/admin_login.html')


def admin_dashboard(request):
    # Get the total number of users
    total_users = User.objects.count()
    
    # Get the total number of non-staff users
    non_staff_users = User.objects.filter(is_staff=False)
    
    # Get the total number of books
    total_books = Book.objects.count()

    # Get the number of active users (active users are those who have logged in recently)
    # Active users are those who have logged in within the last 30 days (you can adjust the filter)
    active_users = User.objects.filter(is_active=True)

    # Get recent activities for non-staff and staff users
    recent_non_staff_activities = non_staff_users.order_by('-last_login')[:5]  # Get the 5 most recent non-staff users' activities
    recent_admin_activities = User.objects.filter(is_staff=True).order_by('-last_login')[:5]  # Get the 5 most recent admin activities

    # Pass the data to the template
    context = {
        'total_users': total_users,
        'non_staff_users': non_staff_users.count(),
        'total_books': total_books,
        'active_users': active_users.count(),
        'recent_non_staff_activities': recent_non_staff_activities,
        'recent_admin_activities': recent_admin_activities,
    }

    return render(request, 'control_panel/admin_dashboard.html', context)


def admin_manage_users(request):
    
    users = User.objects.all()

    
    action = request.GET.get('action')
    user_id = request.GET.get('user_id')
    
    if action and user_id:
        try:
            user = User.objects.get(id=user_id)
            
            if action == 'delete':
                
                if user.is_superuser:
                    messages.error(request, "You cannot delete a superuser.")
                else:
                    user.delete()
                    messages.success(request, "User deleted successfully.")
            elif action == 'suspend':
                #
                user.is_active = False
                user.save()
                messages.success(request, "User suspended successfully.")
        except User.DoesNotExist:
            messages.error(request, "User not found.")
    
    
    users = User.objects.all()

    
    context = {
        'users': users,
    }

    return render(request, 'control_panel/manage_users.html', context)


def admin_add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_manage_users')  # Redirect to the manage users page after success
    else:
        form = UserForm()
    return render(request, 'control_panel/add_user.html', {'form': form})

# Edit User Function
def edit_user(request, user_id):
    # Get the user object based on user_id
    user = get_object_or_404(User, id=user_id)

    # If the request method is POST, process the form data
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()  # Save the updated user data
            return redirect('admin_manage_users')  # Redirect to the manage users page (you can change this URL as needed)
    else:
        # If it's a GET request, just display the form with the user's current data
        form = UserForm(instance=user)

    # Render the 'edit_user' template with the form
    return render(request, 'control_panel/edit_user.html', {'form': form, 'user': user})

def suspend_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    # Here you can suspend the user, e.g., by setting the is_active field to False
    user.is_active = False
    user.save()

    # Optionally, you can redirect back to the manage users page with a success message
    return redirect('control_panel/admin_manage_users')

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    # You can delete the user
    user.delete()

    # Optionally, redirect back to the manage users page
    return redirect('control_panel/admin_manage_users')

def admin_manage_books(request):
    # Query all books from the database
    books = Book.objects.all()  # Fetch all books
    
    print(books)  # Debugging line to print the queryset
    
    return render(request, 'control_panel/manage_books.html', {'books': books})


class AddBookView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'control_panel/add_book.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            print("Form is valid, saving book...")
            form.save()  # Save the new book to the database
            return redirect('admin_manage_books')  # Redirect to the books management page
        else:
            print("Form is not valid. Errors:")
            print(form.errors)  # Output form errors in the console
        return render(request, 'control_panel/add_book.html', {'form': form})


def admin_edit_book(request, book_id):
    # Retrieve the book object using the book_id (primary key)
    book = get_object_or_404(Book, pk=book_id)
    
    # If the request method is POST, handle the form submission
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            # Save the updated book information
            form.save()
            # Redirect to the book management page (or anywhere you want)
            return redirect('control_panel:admin_manage_books')  # Adjust the redirect URL as necessary
    else:
        # If GET request, display the form with the current book data
        form = BookForm(instance=book)
    
    # Render the form in the template
    return render(request, 'control_panel/edit_book.html', {'form': form, 'book': book})

def admin_publish_book(request, book_id):
    # Retrieve the book object by ID
    book = get_object_or_404(Book, pk=book_id)
    
    # Set the 'is_published' field to True
    book.is_published = True
    book.save()  # Save the changes to the database
    
    # Redirect to the manage books page
    return redirect('control_panel/manage_books.html')

def admin_delete_book(request, book_id):
    # Retrieve the book object by ID, or return 404 if not found
    book = get_object_or_404(Book, pk=book_id)
    
    # Delete the book from the database
    book.delete()
    
    # Redirect to the manage books page after deletion
    return redirect('admin_manage_books')
                        
def admin_settings(request):
    if request.method == "POST":
        form = SettingsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_settings')
    else:
        settings = Settings.objects.first()  # Fetch the first settings record
        form = SettingsForm(instance=settings) if settings else SettingsForm()

    return render(request, 'control_panel/settings.html', {'form': form, 'site_name': settings.site_name, 'admin_email': settings.admin_email, 'contact_info': settings.contact_info, 'theme': settings.theme})

def admin_logout(request):
    if request.method == 'POST':  # If the user clicks the "Log Out" button
        logout(request)  # Log the user out
        return redirect('admin_login')  # Redirect to the admin login page
    return render(request, 'control_panel/admin_logout.html')