from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.core.files.storage import FileSystemStorage
from .models import *

# Create your views here.

def indexV(request):
    a=UserProfileM.objects.all()
    return render(request,'index.html',{'a':a})

def mainV(request):
    return render(request,'pages/main.html')


def logingV(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        user = auth.authenticate(username=name, password=password)
        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                # return redirect(request.POST.get('next'))
                return redirect('/')
            else:
                return redirect('/')
        else:
            messages.info(request, 'User is not valid')
            return redirect('/login/')
    else:
        return render(request,'pages/login.html')

def loguotV(request):
    auth.logout(request)
    return redirect('/login/')

def createuserV(request):
    if request.method == 'POST' and request.FILES:
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        present = request.POST.get('present')
        permanent = request.POST.get('permanent')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User Name already taken')
                return redirect('/Singup/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'E-Mail already taken')
                return redirect('/Singup/')
            else:
                image = request.FILES['image']
                store = FileSystemStorage()
                filename = store.save(image.name, image)
                profile_pic_url = store.url(filename)
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                sing = UserProfileM(user=user,Phone=phone, Present_Address=present, Permanant_Address=permanent, Image=filename)
                sing.save()
                messages.info(request, 'Data Saved')
                return redirect('/create/user/')
        else:
            messages.info(request, 'password donot match')
            return redirect('/create/user/')
    else:
        return render(request,'admin/usercreate.html')


def DashboardV(request):
    return render(request,'pages/Dashboard.html')
def admindashboardV(request):
    return render(request,'admin/Dashboard.html')

def inventorydashboardV(request):
    return render(request,'inventory/Dashboard.html')

def itemnameV(request):
    item=ItemEntryM.objects.all()
    return render(request,'inventory/itementry.html',{'item':item})

def itemnameSaveV(request):
    if request.method=='POST':
        itemnames=request.POST.getlist('itemname')
        units=request.POST.getlist('unit')
        c=min([len(itemnames),len(units)])
        for i in range(c):
            data=ItemEntryM.objects.create(Itemname=itemnames[i],Unit=units[i])
            messages.info(request, 'Data Save')
    return redirect('/item/entry/')

def itemnameeditV(request,id=0):
    item = ItemEntryM.objects.all()
    if id !=0:
        itemedit=ItemEntryM.objects.filter(pk=id)
    return render(request, 'inventory/itementryedit.html',{'itemedit':itemedit,'item':item})

def itemnameupdateV(request,id=0):
    if id !=0:
        if request.method=='POST':
            itemnames = request.POST.get('itemname')
            units = request.POST.get('unit')
            update=ItemEntryM.objects.get(pk=id)
            update.Itemname=itemnames
            update.Unit=units
            update.save()
            messages.info(request, 'Data Update')
    return redirect('/item/entry/')

def itemnamedeleteV(request,id=0):
    if id !=0:
        data = ItemEntryM.objects.get(pk=id)
        data.delete()
        messages.info(request, 'Data Delete')

    return redirect('/item/entry/')


def suppliernameV(request):
    return render(request,'inventory/supplier.html')

def suppliernameSaveV(request):
    if request.method=='POST':
        name=request.POST.get('suppliername')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        datasave=SupplierInfoM.objects.create(Suppliername=name,Address=address,Phone=phone,Email=email)
        messages.info(request, 'Data Save')
    return redirect('/upplier/entry/')

def suppliernameeditV(request):
    pass

def suppliernameupdateV(request):
    pass
def suppliernamedeleteV(request):
    pass


