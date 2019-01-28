from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    testType = "Lorem ipsum dolor sit amet consectetur adipiscing elit euismod ac dictum, egestas odio nec risus posuere fusce cursus ultrices varius. Id etiam montes et est facilisi gravida mus interdum quis platea sem felis tempus dis bibendum, fermentum volutpat faucibus fringilla parturient primis semper justo netus per tortor nullam magna iaculis."
    return render(request, 'index.html', {'text': testType})

# def logon(request):
    # loginTest = "Sorry, Enter valid credentials"
#     # username = request.POST('username')
#     # password = request.POST('password')
#     # user
    # return render(request, 'registration/login.html', {'lgtest': loginTest})

def signup(request):
    signUp = "SignUp Page"
    return render(request, 'signup.html', {'lgtest': signUp})

# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return render(request, 'admin/')
#     else:
#         return HttpResponse("Wrong Credentials")
        