from django.shortcuts import render,redirect
from .models import *
from housing_socity import models
from datetime import date

# Create your views here.
def member_index(request):
    events=models.Event.objects.all()
    return render(request,'member-index.html',{'events':events})


def member_login(request):
    try:
        user = Member.objects.get(email=request.session['memail'])
        return render(request,'member-index.html',{'user':user})
    except:
        if request.method == 'POST':  
            try:
                user = Member.objects.get(email=request.POST['email'])
                if request.POST['Password'] == user.Password and user.verify:
                    request.session['memail'] = user.email
                    return redirect('member-index')
                return render(request,'member-login.html',{'msg':'Password is incorrect'})
            except:
                return render(request,'member-login.html',{'msg':'Account not found'})
        
        return render(request,'member-login.html')
    
def member_logout(request):
    del request.session['memail']
    return redirect('member-login')

def create_complain(request):
    if request.POST:
        user=Member.objects.get(email=request.session['memail'])
        models.Complain.objects.create(
            complain_by=user,
            subject=request.POST['subject'],
            des=request.POST['des'],
            pic=request.FILES['pic'] if request.FILES else None
        )
    return render(request,'create-complain.html')

def my_complains(request):
    user=Member.objects.get(email=request.session['memail'])
    complains=models.Complain.objects.filter(complain_by=user)
    return render(request,'my-complains.html',{'complains':complains})

def my_notice(request):
    user=Member.objects.get(email=request.session['memail'])
    notices=models.Notice.objects.filter(send_to=user)
    return render(request,'my-notice.html',{'notice':notices})    