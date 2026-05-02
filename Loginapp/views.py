from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login 
# Create your views here.
def register(request):
    if request.method == 'POST':
        a=request.POST.get('username')
        b=request.POST.get('password')
        if User.objects.filter(username=a).exists():
            return render(request, 'register.html',{'error':'Username already exists'})
        User.objects.create_user(username=a,password=b)
        return redirect('index')
    return render(request, 'register.html')
def login_view(request):
    if request.method == 'POST':
        a = request.POST.get('username')
        b = request.POST.get('password')
        user = authenticate(request, username=a, password=b)

        if user:
            login(request, user)  # now correctly calls Django login
            return redirect('dashboard')
        else:
            return render(request, 'index.html', {'error': 'Invalid username or password'})

    return render(request, 'index.html')    
def dashboard(request):
    return render(request, 'dashboard.html')
