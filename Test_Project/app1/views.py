
# Create your views here.
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import *
from .serializers import UserSerializer
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from Test_Project import settings as se
import random
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
login_otp = None

def user_signup(request):

    """
        Creating new user and sending static password to user mail 
    """

    if request.method == "POST":
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "User already existed")

        else:
            user = CustomUser(email=email, first_name=fname, last_name=lname, gender=gender, phone_number=phone)
            user.set_password(se.USER_PASSWORD)
            user_password = se.USER_PASSWORD
            subject = "Password to login"
            message = f"Dear Customer Thank you for Registering Account. Use this password to login: {user_password}"
            send_mail(subject, message, se.EMAIL_HOST_USER, [email], fail_silently=False)
            user.save()
            messages.success(request, "User Created Successfully. pls check your email")

    return render(request, 'signup.html')

@csrf_exempt
def user_login(request):

    """
        Login user and sending random OTP to user mail 
    """

    if request.method == "POST":
        email = request.POST.get('email')
        ps = request.POST.get('password')
        user = authenticate(request, email=email, password=ps)
        if user is not None:
            request.session['user'] = email
            global login_otp

            login_otp = random.randint(1,10000)
            subject = "OTP to login"
            message = f"Use this password to login: {login_otp}"
            send_mail(subject, message, se.EMAIL_HOST_USER, [email], fail_silently=False)
            return render(request, "validate_otp.html")
        else:
            messages.error(request, "Invalid user")
            return redirect('user_login')
        
    return render(request, 'login.html')

@csrf_exempt
def validate_otp(request):

    """
        Verifying user OTP if valid logging in  
    """
    
    if request.method == "POST":
        otp = request.POST.get('otp')
        global login_otp
        if otp == str(login_otp):
            if 'user' in request.session:
                email = request.session['user']
                try:
                    login_user = CustomUser.objects.get(email=email)
                except CustomUser.DoesNotExist:
                    return redirect('user_login')
                
                login(request, login_user)
                return render(request, "dashboard.html")
            else:
                return redirect('user_login')
        else:
            messages.error(request, "Invalid OTP")
            return redirect('validate_otp')
        
    return render(request, "validate_otp.html")

@login_required(login_url='user_login')
def dashboard(request):

    """
        User Dashboard page after successfully logged in
    """
    
    return render(request, "dashboard.html")

@csrf_exempt
def auto_suggest(request):

    """
        This is auto suggest function invoke when user type something in input
        it will fetch all the input data from database and auto populate on input
        User can search based on city, country, country language 
    """

    query = request.GET.get("query")
    print("query::::", query)

    l_result = []
    country_obj = Country.objects.filter(
            name__icontains=query
        ).values('name', 'code', 'population')
    l_result = list(country_obj)

    if not l_result:
        country_lan = countrylanguage.objects.filter(
            language__icontains = query
        ).values('language','countrycode')
        l_result = list(country_lan)

    if not l_result:

        city_obj = city.objects.filter(
            name__icontains = query
        ).values('name', 'countrycode', 'district')
        l_result = list(city_obj)
            
    print("l_result:::::::", l_result)
    return JsonResponse(l_result, safe=False)

@csrf_exempt
@login_required(login_url='user_login')
def search(request):

    """
        Quering the input and showing all the results in search page
    """

    context = {}
    if request.method == "POST":
        query = request.POST.get("query")

        """
            Fetching Country data with associated cities and city languages
        """
        try:
            country_obj = Country.objects.get(
                name__iexact = query
            )
            city_obj = city.objects.filter(countrycode= country_obj)
            country_lan = countrylanguage.objects.filter(countrycode= country_obj)
            context.update({"country":country_obj, "city":city_obj, "country_lan":country_lan})
        except:
            
            """
                Fetching Country language data with associated country and cities
            """
            
            if not context:
                country_lan = countrylanguage.objects.filter(
                    language__iexact = query
                ).order_by('percentage')
                for c_lan in country_lan:
                    c_code = c_lan.countrycode.code
                    country_obj = Country.objects.get(code=c_code)
                    city_obj = city.objects.filter(countrycode= country_obj).order_by('-population')
                    context.update({"country": country_obj, "city":city_obj})
                context.update({"country_lan":country_lan})

            """
                Fetching City data with associated country and country langugages
            """

            if not country_lan:
                city_obj = city.objects.filter(
                name__iexact = query
                ).order_by('-population')
                for ct in city_obj:
                    c_code = ct.countrycode.code
                    country_obj = Country.objects.get(code=c_code)
                    country_lan = countrylanguage.objects.filter(countrycode=country_obj).order_by('-percentage')
                    context.update({"country": country_obj, "country_lan": country_lan})
                context.update({"city":city_obj})

    print("context:::::::", context)
    return render(request, "search.html", context)

@login_required(login_url='user_login')
def user_logout(request):

    """
        logout user 
    """

    logout(request)
    return redirect("user_login")


#####################################################
#####################################################

@csrf_exempt
@api_view(['POST', 'GET'])
def user_signup_api(request):

    """
        API to create new user  
    """

    if request.method == "POST":
        obj = UserSerializer(data= request.data)
        if obj.is_valid():
            obj.save()
            return Response({"Success": "User Created Successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"Error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def user_login_api(request):

    """
        API to login user  
    """

    if request.method == "POST":
        email = request.data['email']
        ps = request.data['password']
        user = authenticate(request, email=email, password=ps)
        if user is not None:
            login(request, user)
            return Response({"Success":"User logged in successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"Error":"Invalid User"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def user_logout_api(request):

    """
        API to logout user  
    """

    if request.method == "POST":
        logout(request)
        return Response({'Success':'User logged out successfully'}, status=status.HTTP_200_OK)

    

########################### end ###############################3




