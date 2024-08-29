# from django.http import HttpResponse

# def Home(request):
#     return HttpResponse("Hello, welcome to the home page!")



#----


from django.shortcuts import render


def Home(request):
    return render(request, 'myapp/home.html')


#myvenv/Scripts/activate
#cd myproject
#python manage.py migrate
#python manage.py runserver