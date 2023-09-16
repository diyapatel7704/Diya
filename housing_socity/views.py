from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from Members.models import *
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def pricing(request):
    return render(request,'pricing.html')

def services(request):
    return render(request,'services.html')

def login(request):
    try:

        user=housing_socity.get(email=request.session['email'])
        return render(request,'about.html',{'user':user})
    except:

        if request.method == 'POST':
            try:
                user = housing_socity.objects.get(email=request.POST['email'])
                if request.POST['Password'] == user.Password:
                    request.session['email'] = user.email
                    return render(request,'about.html',{'user':user})
                return request(request,'login.html',{'msg':'Incorrect Password'})
                
            except:
                return render(request,'signup.html',{'msg':'Account does not exist please sign up'})

        return render(request,'login.html')

def signup(request):
    if request.method =='POST':
        if request.POST['Password'] == request.POST['cpassword']:
            try:
                housing_socity.objects.get(email=request.POST['email'])
                return render(request,'login.html',{'msg':'Account already exist please sign in'})
            except:
                housing_socity.objects.create(
                    name=request.POST['name'],
                    email=request.POST['email'],
                    Mobile=request.POST['Mobile'],
                    Address=request.POST['Address'],
                    Password=request.POST['Password']        
            )
            return render(request,'login.html',{'msg':'Account created go and login'})
        
        return render(request,'signup.html',{'msg':'Both password are not same'})
    
    return render(request,'signup.html')

def logout(request):
    del request.session['email']
    return redirect('login')

def change_password(request):
    #try: 
        user =housing_socity.objects.get(email=request.session['email'])
        if request.POST:
            if request.POST['oPassword'] == user.Password:
                if request.POST['nPassword'] == request.POST['cPassword']:
                    user.Password = request.POST['nPassword']
                    user.save()
                    return render(request,'change_password.html',{'msg':'Password Updated','user':user})
                return render(request,'change_password.html',{'msg':'New passwords are not matching','user':user})
            return render(request,'change_password.html',{'msg':'Old password incorrect','user':user})
        return render(request,'change_password.html',{'user':user})
    #except:
        return render(request,'login.html',{'msg':"Sign in first"})
    
def edit_profile(request):
    try:
        user=housing_socity.objects.get(email=request.session['email'])
        if request.POST:
            user.name = request.POST['name']
            user.Mobile = request.POST['Mobile']
            user.Address = request.POST['Address']
            if 'pic' in request.FILES:
                user.profile_pic = request.FILES['pic']
            user.save()
        return render(request,'edit_profile.html',{'user':user})
    except:
        return render(request,'login.html')
    
def member_detail(request):
    try:
        user=housing_socity.objects.get(email=request.session['email'])
        members = Member.objects.all()

        return render(request,'member_detail.html',{'user':user,'members':members})
    except:
        return render(request,'login.html')
        
       
def edit_member(request,pk):
    try:
        user = housing_socity.objects.get(email=request.session['email'])
        member = Member.objects.get(id=pk)
        if request.method == 'POST':
            member.fname = request.POST['fname']
            member.res_type = request.POST['res_type']
            member.verify = True if 'verify' in request.POST  else False
            member.save()
            return redirect('member_detail')
            
        return render(request,'edit_member.html',{'user':user,'member':member,'res_from':str(member.res_from)})
    except:
        return redirect('login')
    
def manage_events(request):
    user=housing_socity.objects.get(email=request.session['email'])
    events = Event.objects.all()[::-1]
    return render(request,'manage_events.html',{'user':user,'events':events})       
        
def view_event(request,pk):
    user = housing_socity.objects.get(email=request.session['email'])
    event=Event.objects.get(id=pk)
    return render(request,'view_event.html',{'user':user,'event':event,'eventdate':str(event.date)})

def delete_event(request,pk):
    event= Event.objects.get(id=pk)
    event.delete()
    return redirect('manage_events')

def add_event(request):
    user=housing_socity.objects.get(email=request.session['email'])
    if request.method == 'POST':
        if 'pic' in request.FILES:
            Event.objects.create(
                created_by = user,
                subject =request.POST['subject'],
                des = request.POST['des'],
                date = request.POST['date'],
                pic = request.FILEAS['pic']

            )
        else:
            Event.objects.create(
                created_by = user,
                subject =request.POST['subject'],
                des = request.POST['des'],
                date = request.POST['date']
            )
        return redirect('manage_events')

    return render(request,'add-event.html',{'user':user})

def manage_complain(request):
    user= housing_socity.objects.get(email=request.session['email'])
    complains = Complain.objects.all()
    return render(request,'manage-complain.html',{'complains':complains,'user':user})
    
def view_complain(request,pk):
    user = housing_socity.objects.get(email=request.session['email'])
    complain = Complain.objects.get(id=pk)
    return render(request,'view-complain.html',{'complain':complain,'user':user})

def solve_complain(request,pk):
    user = housing_socity.objects.get(email=request.session['email'])
    complain = Complain.objects.get(id=pk)
    complain.solve = True
    complain.solve_by = user
    complain.solve_on = datetime.now()
    complain.save()
    return redirect('manage-complain')

def manage_notice(request):
    user = housing_socity.objects.get(email=request.session['email'])
    notices=Notice.objects.all()
    return render(request,'manage-notice.html',{'user':user,'notices':notices})

def new_notice(request):
    user = housing_socity.objects.get(email=request.session['email'])
    members = Member.objects.filter(verify=True)
    return render(request,'new-notice.html',{'user':user,'members':members})
   
   
def view_notice(request,pk):
    user = housing_socity.objects.get(email=request.session['email'])
    notices = Notice.objects.get(id=pk)
    return render(request,'view-notice.html',{'notices':notices,'user':user})
