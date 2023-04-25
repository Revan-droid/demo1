from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

import joblib
from sklearn.preprocessing import MinMaxScaler
import numpy as np

#with open('ML_models\lr_bin.joblib', 'rb') as f:
    #loaded_lr_model =joblib.load(f)


loaded_rf_model = joblib.load("ML_models/rf_bin.joblib")
loaded_lsvm_model = joblib.load("ML_models/lsvm_multi.joblib")

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def ResultsPage(request):
    if request.method == 'POST':
        rate=request.POST.get('rate','default')
        sttl=request.POST.get('sttl','default')
        sload=request.POST.get('sload','default')
        dload=request.POST.get('dload','default')
        ct_srv_src=request.POST.get('ct_srv_src','default')
        ct_state_ttl=request.POST.get('ct_state_ttl','default')
        ct_dst_ltm=request.POST.get('ct_dst_ltm','default')
        ct_src_dport_ltm=request.POST.get('ct_src_dport_ltm','default')
        ct_dst_sport_ltm=request.POST.get('ct_dst_sport_ltm','default')		
        ct_dst_src_ltm=request.POST.get('ct_dst_src_ltm','default')
        ct_src_ltm=request.POST.get('ct_src_ltm','default')
        ct_srv_dst=request.POST.get('ct_srv_dst','default')
        state_CON=request.POST.get('state_CON','default')
        state_INT=request.POST.get('state_INT','default')
        labels=[[float(rate),
                 float(sttl),
                 float(sload),
                 float(dload),
                 float(ct_srv_src),
                 float(ct_state_ttl),
                 float(ct_dst_ltm),
                 float(ct_src_dport_ltm),
                 float(ct_dst_sport_ltm),
                 float(ct_dst_src_ltm),
                 float(ct_src_ltm),
                 float(ct_srv_dst),
                 float(state_CON),
                 float(state_INT)]]
        our_labels = loaded_rf_model.predict(labels)
        print(our_labels)
        round = lambda x:1 if x>=0.5 else 0
        b=round(our_labels)
        if b==1:
            a="Normal"
        if b==0:
            a="Abnormal"
        details={
            "answer":b,
            "attack":a,
        }
        return render(request,'results.html',details)
     
    return (request,'results.html')

def ResultsPage2(request):
    if request.method == 'POST':
        dttl=request.POST.get('dttl','default')
        swin=request.POST.get('swin','default')
        dwin=request.POST.get('dwin','default')
        tcprtt=request.POST.get('tcprtt','default')
        synack=request.POST.get('synack','default')
        ackdat=request.POST.get('ackdat','default')
        proto_tcp=request.POST.get('proto_tcp','default')
        proto_udp=request.POST.get('proto_udp','default')
        service_dns=request.POST.get('service_dns','default')		
        state_CON=request.POST.get('state_CON','default')
        state_FIN=request.POST.get('state_FIN','default')
        attack_cat_Analysis=request.POST.get('attack_cat_Analysis','default')
        attack_cat_DoS=request.POST.get('attack_cat_DoS','default')
        attack_cat_Exploits=request.POST.get('attack_cat_Exploits','default')
        attack_cat_Normal=request.POST.get('attack_cat_Normal','default')
        labels=[[float(dttl),
                 float(swin),
                 float(dwin),
                 float(tcprtt),
                 float(synack),
                 float(ackdat),
                 float(proto_tcp),
                 float(proto_udp),
                 float(service_dns),
                 float(state_CON),
                 float(state_FIN),
                 float(attack_cat_Analysis),
                 float(attack_cat_DoS),
                 float(attack_cat_Exploits),
                 float(attack_cat_Normal)
                ]]
        our_labels = loaded_lsvm_model.predict(labels)
        print("our_labels")
        round = lambda x:1 if x>=0.5 else 0
        x = int(our_labels)
        y = our_labels-x
        z=round(y)
        if z==1 :
           b=x+1
        b=x
        if b==0:
            a="Analysis"
        elif b==1:
            a="Backdoor"
        elif b==2:
            a="DoS"
        elif b==3:
            a="Exploits"
        elif b==4:
            a="Fuzzers"
        elif b==5:
            a="Generic"
        elif b==6:
            a="Normal"
        elif b==7:
            a="Reconnaissance"
        else :
            a="Worms"

        details={
            "answer":b,
            "attack":a,
        }
        return render(request,'results.html',details)

def Mclassified(request):
    if(request.method=='POST'):
        val=request.POST.get('hi')
        if(val == 'MUL'):
            return render(request,'Mclassified.html')
        else:
            return render(request,'Bclassified.html')
    return (request,'home.html')

def Bclassified(request):
    return (request,'Bclassified.html')

def SignUpPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render (request,'incorrect password.html')
    return render (request,'login.html')
          
def LogoutPage(request):
    logout(request)
    return redirect('login')

def classified2(request):
    return render (request,'Analysis Of Dataset/classified2.html')

def classifiedmul(request):
    return render (request,'Analysis Of Dataset/classifiedmul.html')

def correlation2(request):
    return render (request,'Analysis Of Dataset/correlation2.html')

def correlationmul(request):
    return render (request,'Analysis Of Dataset/correlationmul.html')

def dt(request):
    return render (request,'Binary Labels/dt.html')

def knn(request):
    return render (request ,'Binary Labels/knn.html')

def lg(request):
    return render(request ,'Binary Labels/lg.html')

def lrg(request):
    return render(request,'Binary Labels/lrg.html')

def lsvm(request):
    return render(request,'Binary Labels/lsvm.html')

def rf(request):
    return render(request,'Binary Labels/rf.html')

def dtm(request):
    return render (request,'Multi Labels/dtm.html')

def knnm(request):
    return render (request ,'Multi Labels/knnm.html')

def lgm(request):
    return render(request ,'Multi Labels/lgm.html')

def lrgm(request):
    return render(request,'Multi Labels/lgrm.html')

def lsvmm(request):
    return render(request,'Multi Labels/lsvmm.html')

def rfm(request):
    return render(request,'Multi Labels/rfm.html')

def dtr(request):
    return render (request,'results/dt_bin_results.html')

def knnr(request):
    return render (request ,'results/knn_bin_results.html')

def lgr(request):
    return render(request ,'results/lr_bin_results.html')

def lrgr(request):
    return render(request,'results/logr_bin_results.html')

def lsvmr(request):
    return render(request,'results/lsvm_bin_results.html')

def rfr(request):
    return render(request,'results/rf_bin_results.html')