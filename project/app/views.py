from django.shortcuts import render
from .models import *

# Create your views here.
def registerpage(request):
    return render(request,'register.html')

def register(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    cpassword = request.POST.get('cpassword')

    user = User.objects.filter(email=email)

    if user:
        msg = "Email exist"
        return render(request,'login.html',{'msg':msg})
    else:
        if password == cpassword:
            user = User.objects.create(
                fname = fname,
                lname = lname,
                email = email,
                password = password
            )
            user.save()
            msg = "Registration successful"    
            return render(request,'login.html',{'msg':msg})
        else:
            msg = "Password not match"
            return render(request,'register.html',{'msg':msg})
        
def loginpage(request):
    return render(request,'login.html')

def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = User.objects.filter(email=email)
    if user:
        data = User.objects.get(email=email)
        if data.password == password:
            fname = data.fname
            lname = data.lname
            email = data.email
            password = data.password
            
            request.session['fname']=fname
            request.session['lname']=lname
            request.session['email']=email
            request.session['pass']=password


            key = {'fname':fname,'lname':lname,'email':email , 'password':password}

            return render(request,'home.html',{'key':key})
        else:
            msg = "Password does not match"
            return render(request,'login.html',{'msg':msg})
    else:
        msg = "Email does not exist"
        return render(request,'register.html',{'msg':msg})    

def logout(request):
    
    del request.session['fname']
    del request.session['lname']
    del request.session['email']
    del request.session['pass']
    request.session.flush()
    return render(request,'login.html')

def insert(request):
    email = request.POST.get('email')
    query = request.POST.get('query')
    
    query = Query.objects.create(Email=email,query=query)
    query.save()

    fname=request.session['fname']
    lname=request.session['lname']
    email=request.session['email']
    password=request.session['pass']


    key = {'fname':fname,'lname':lname,'email':email , 'password':password}
    data = Query.objects.filter(Email=email)
    return render(request,'home.html',{'key':key,'data':data})

def queryshow(request,pk):
    data = Query.objects.filter(Email=pk)

    fname=request.session['fname']
    lname=request.session['lname']
    email=request.session['email']
    password=request.session['pass']
    
    key = {'fname':fname,'lname':lname,'email':email , 'password':password}

    return render(request,'home.html',{'key':key,'data':data})

def delete(request,pk):
    data = Query.objects.get(id=pk)
    data.delete()
    fname=request.session['fname']
    lname=request.session['lname']
    email=request.session['email']
    password=request.session['pass']

    key = {'fname':fname,'lname':lname,'email':email , 'password':password}
    data = Query.objects.filter(Email=email)

    return render(request,'home.html',{'key':key,'data':data})  

def edit(request,pk):
    data = Query.objects.get(id=pk)
    id= data.id
    email = data.Email
    query = data.query
    fname=request.session['fname']
    lname=request.session['lname']
    email=request.session['email']
    password=request.session['pass']

    key = {'fname':fname,'lname':lname,'email':email, 'password':password}
    data1 = {'id':id,'email':email,'query':query}
    data2 = Query.objects.filter(Email=email)
    return render(request,'home.html',{'key':key,'key1':data1,'data':data2})

def update(request,pk):
    print(pk)
    email = request.POST['email']
    query = request.POST['query']
    data = Query.objects.get(id=pk)
    data.Email = email
    data.query = query
    data.save()

    fname=request.session['fname']
    lname=request.session['lname']
    email=request.session['email']
    password=request.session['pass']

    key = {'fname':fname,'lname':lname,'email':email, 'password':password}
    data2 = Query.objects.filter(Email=email)   

    return render(request,'home.html',{'key':key,'data':data2})