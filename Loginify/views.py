from django.http import HttpResponse, JsonResponse
from .models import UserDetails
from .serializers import UserDetailsSerializer
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render, redirect


def print_hello(request):
    return HttpResponse("Hello, world!")

@csrf_exempt
def user_data(request):
    if request.method=="GET":
        try:
            all_users = UserDetails.objects.all()
            serializer_data=UserDetailsSerializer(all_users,many=True)
            return JsonResponse(serializer_data.data,safe=False)
        except Exception as e:
            return JsonResponse({
                "error": str(e)
            },status=500)
            
    if request.method=="POST":
        input_data=json.loads(request.body)
        serializer_data=UserDetailsSerializer(data=input_data)
        try:
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({
                    "Success":True,
                    "message":"Data saved successfully",
                    "data": serializer_data.data},status=201)
            else:
                return JsonResponse(serializer_data.errors,status=400)
        except Exception as e:
            return JsonResponse({
                "error": str(e)
            },status=500)
            
@csrf_exempt        
def single_user_data(request,pk):
    if request.method == "GET":
        try:
            user=UserDetails.objects.get(pk=pk)
            serializer_data=UserDetailsSerializer(user)
            return JsonResponse(serializer_data.data,safe=False)
        except UserDetails.DoesNotExist:
            return JsonResponse({
                "error":"User not found"
            },status=404)
        except Exception as e:
            return JsonResponse({
                "error": str(e)
            },status=500)
            
    if request.method=="DELETE":
        try:
            user=UserDetails.objects.get(pk=pk)
            return JsonResponse({
                "Success": True,
                "message":"Data delete successfully"
            },status=204)
        except Exception as e:
            return JsonResponse({
                "error": str(e)
            },status=500)
            
    if request.method=="PATCH":
        try:
            user =UserDetails.objects.get(pk=pk)
            input_data= json.loads(request.body)
            serializer_data =UserDetailsSerializer(user,data=input_data,partial=True)
            
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({
                    "Success":True,
                    "message":"Data updated successfully",
                    "data": serializer_data.data
                }, status=200)
            else:
                return JsonResponse(serializer_data.errors, status=400)
        except Exception as e:
            return JsonResponse({
                "error": str(e)
            },status=500)
            
def signup(request):
    if request.method == "POST":
        data = {
            'username': request.POST.get('username'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password')
        }
        serializer = UserDetailsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                    "Success":True,
                    "message":"Data saved successfully",
                    "data": serializer.data},status=201)
        return render(request, 'loginify/signup.html', {'errors': serializer.errors})

    return render(request, 'loginify/signup.html')

def login(request):
    if request.method == "POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = UserDetails.objects.get(username=username)

            if user.password == password:
                request.session['username'] = user.username  
                return JsonResponse({
                    "Success":True,
                    "message":"Login successfully"},status=200)  
            else:
                return render(request, 'loginify/login.html', {'error': 'Invalid password'})
        
        except UserDetails.DoesNotExist:
            return render(request, 'loginify/login.html', {'error': 'Invalid username'})

    return render(request, 'loginify/login.html')
