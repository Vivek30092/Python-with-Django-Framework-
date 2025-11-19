from django.shortcuts import render
from villaAgency.models import SignUp
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def contact(request):
    return render(request, 'contact.html')

def index(request):
    return render(request, 'index.html')

def properties(request):
    return render(request, 'properties.html')

def property_details(request):
    return render(request, 'property-details.html')

def signup(request):
    if request.method == 'POST':
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        mob1 = request.POST.get('mobileNumber')
        unm1 = request.POST.get('username')
        pw1 = request.POST.get('password')

        if User.objects.filter(username=unm1).exists():
            messages.error(request, "Username already taken, choose another one.")
            return render(request, 'signup.html')
        user = User.objects.create_user(username=unm1, password=pw1)
        user.save()

        form = SignUp(name=name1, email=email1, mobilenumber=mob1, username=unm1, password=pw1)
        form.save()
        # print(name1, email1, mob1, unm1, pw1)

        return render(request, 'login.html')
    else:
        return render(request, 'signup.html')

def login(request):
    request.session.flush()
    if request.method == 'POST':
        unm1 = request.POST.get('unm')
        pw1 = request.POST.get('pw')
        try:
            data = Customer.objects.get(pw=pw1)
            request.session['name'] = unm1
            request.session['data'] = data.id 
            return redirect('/')
        except Exception:
            return render(request,'login.html')
    else:
        return render(request,'login.html')