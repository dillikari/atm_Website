from django.shortcuts import render
from appATM.models import CustomerAccount
from django.db.models import F,Q
import numpy as np
# Create your views here.

def functionOne(request):
    return render(request,'index.html')

def functionTwo(request):
        if request.method=='POST':
            accNumber=int(request.POST.get('accountNumber'))
            custName=request.POST.get('customerName')
            pinCode=int(request.POST.get('pinNumber'))
            custAge=int(request.POST.get('customerAge'))
            custMobile=int(request.POST.get('customerMobile'))
            custAadhaar=int(request.POST.get('customerAadhaar'))
            custAddress=request.POST.get('customerAddress')
            custState=request.POST.get('customerState')
            customerdata=CustomerAccount.objects.create(
                account_Number=accNumber,
                customer_Name=custName,
                pin_Number=pinCode,
                customer_Age=custAge,
                mobile_Number=custMobile,
                customer_Aadhaar=custAadhaar,
                customer_Address=custAddress,
                customer_State=custState
            )
            return render(request,'createaccount.html',context={'msg':'Customer Account is Created'})
        else:
            return render(request,'createaccount.html')




# def functionThree(request):
#     if request.method=="POST":
#         accountNumber=int(request.POST.get('delete'))
#         if CustomerAccount.objects.filter(Q(account_Number=accountNumber)).exists():
#             CustomerAccount.objects.filter(Q(account_Number=accountNumber)).delete()
#             return render(request,'deleteaccount.html',context={'msg':'Your Account is Deleted'})
#         else:
#             return render(request,'deleteaccount.html',context={'msg':'Enter Your Account Number Correctly'})
        
#     return render(request,'deleteaccount.html')


def functionThree(request):
        if request.method=="POST":
            sessioncode=request.session.get('code')
            accountNumber=int(request.POST.get('delete'))
            captcheCode=request.POST.get('captche')
            if CustomerAccount.objects.filter(Q(account_Number=accountNumber)).exists():
                if captcheCode==sessioncode:
                    CustomerAccount.objects.filter(Q(account_Number=accountNumber)).delete()
                    return render(request,'deleteaccount.html',context={'msg':'Your Account is Deleted'})
                else:
                    return render(request,'deleteaccount.html',context={'msg':'Incorrect Captche Code'})
            else:
                return render(request,'deleteaccount.html',context={'msg':'Incorrect Account Number'})
        capital_Letters=[chr(val) for val in range(65,91)]
        small_Letters=[chr(val) for val in range(97,123)]
        numbers=[str(val) for val in range(0,10)]
        combineNumbers=capital_Letters+small_Letters+numbers
        captche1=np.random.choice(combineNumbers,5)
        result="".join(captche1)
        request.session['code']=result
        return render(request,'deleteaccount.html',context={'code':result})



def functionFour(request):
    if request.method=="POST":
        accNumber=int(request.POST.get('accno'))
        pinNumber=int(request.POST.get('pin'))
        amount=float(request.POST.get('amt'))
        account=CustomerAccount.objects.filter(Q(account_Number=accNumber) & Q(pin_Number=pinNumber))
        if account.exists():
            if amount>0:    
                if account.filter(Q(balanceAmount__gte=amount)).exists():
                    account.update(balanceAmount=F('balanceAmount')-amount)
                    return render(request,'widthdrawalamount.html',context={'msg':'Your Amount is Widthdrawal'})
                else:
                    return render(request,'widthdrawalamount.html',context={'msg':' Insufficent Amount'})
            else:
                return render(request,'widthdrawalamount.html',context={'msg':'Enter Amount Greater than zero '})
        else:
            return render(request,'widthdrawalamount.html',context={'msg':'Enter Account or PIN number correctly'})
        
    return render(request,'widthdrawalamount.html')



def functionFive(request):
    if request.method=='POST':
        accountNumber=int(request.POST.get('accno'))
        amount=float(request.POST.get('amt'))
        if CustomerAccount.objects.filter(account_Number=accountNumber).exists():
            if amount>0:
                CustomerAccount.objects.filter(account_Number=accountNumber).update(balanceAmount=F('balanceAmount')+amount)
                return render(request,'depositeamount.html',context={'msg':'Your Amount is Deposited'})
            else:
                return render(request,'depositeamount.html',context={'msg':'Enter Amount Greater Than Zero'})
        else:
            return render(request,'depositeamount.html',context={'msg':'Enter Account Number as correctly'})
    return render(request,'depositeamount.html')




def functionSix(request):
    if request.method=='POST':
        account_Num=int(request.POST.get('accno'))
        accountdetails=CustomerAccount.objects.get(account_Number=account_Num)
        if account_Num==accountdetails.account_Number:
            return render(request,'searchaccount.html',context={'data':accountdetails})
        else:
            return render(request,'searchaccount.html',context={'data':'Please Enter Correct Account Number'})
    return render(request,'searchaccount.html')




def functionSeven(request):
    alldatas=CustomerAccount.objects.all()
    return render(request,'listofcustomer.html',context={'data':alldatas})
    