from django import http
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail


number = []
# Create your views here.
def home(request):
    return render(request, "index.html")

def page1(request):
    data=Todo.objects.all()

    return render(request, "todolist.html", {'todolists' : data , 'command' : 0})

def submit(request):
    obj = Todo()
    obj.title = request.POST['title']
    obj.description = request.POST['description']
    obj.priority = request.POST['priority']
    obj.save()

    return redirect('/1')

def delete(request, id):
    obj = Todo.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return redirect('/1', context=mydictionary)
    #return render(request, "todolist.html", context=mydictionary)

def edit(request, id):
    obj = Todo.objects.get(id=id)
    mydictionary = {
        'title' : obj.title,
        'description' : obj.description,
        'priority' : obj.priority,
        'id' : obj.id
    }
    return render(request, "edit.html", context=mydictionary)

def update(request, id):
    obj = Todo(id=id)
    obj.title = request.POST['title']
    obj.description = request.POST['description']
    obj.priority = request.POST['priority']
    import datetime
    updated_at = datetime.datetime.now()
    obj.created_at=updated_at
    obj.save()
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }

    return redirect('/1')




def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        to_email = request.POST['to-email']
        message = request.POST['message']
        message_email = 'from@example.com'
        # send an email
        send_mail(message_name,
            message,
            message_email,
            [to_email],
            fail_silently=False
            )



        return render(request, "mail.html", {'command' : 1})
    else:
        return render(request, "mail.html", {'command' : 2})




def page3(request):

    return render(request, "3.html" )


def app3(request):

    num = request.POST["number"]
    a_string = str(num)
    letter_list = a_string.split()

    num = list(map(int, letter_list))




    max_num = 0
    max_index = 0
    i = 0
    for x in num:
        if (max_num < x):
            max_num = x
            max_index = i
        i += 1

    print("max=", max_num)
    print("index=", max_index)

    display01 = "ค่ามากสุดคือ " + str(max_num)
    display02 = "ลำดับของค่าที่มากสุด " + str(max_index+1)
    display03 = "indexของค่าที่มากสุด " + str(max_index)



    messages.info(request, display01)
    messages.info(request, display02)
    messages.info(request, display03)


    return render(request, "3.html" , {'num01' : num} )




def page4(request):
    return render(request, "4.html")


def app4(request):

    num = int(request.POST["number"])

    result = 0
    zero_count = 0
    for x in range(num,0,-1):
        if (x == num):
            result += x
        elif (x != num):
            result *= x


    result_str = str(result)
    for y in result_str[::-1] :
        if (y=='0'):
            zero_count += 1
        else:
            break

    display01 = str(num)+"! = "+str(result)
    display02 = "number of consecutive 0 from the back of the line = " + str(zero_count)
    messages.info(request, display01)
    messages.info(request, display02)

    return render(request, "4.html" , {'dis1' : 1} )


def sortdata(request):
    mydictionary={
        "sorted_todos" : Todo.objects.all().order_by('-priority'),
        'command' : 1
    }
    #return redirect('/1', )
    return render(request, "todolist.html", context=mydictionary)

# def searchdata(request):
#     q = request.GET['query']
#     return HttpResponse(q)

def searchdata(request):
    q = request.GET['query']
    mydictionary={
        "search_todos" : Todo.objects.filter(title__contains=q),
        'command' : 2
    }
    return render(request, "todolist.html", context=mydictionary)