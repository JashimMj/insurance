from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.core.files.storage import FileSystemStorage
from .models import *
import datetime
## PDF CODE ###
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



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
    intem=ItemEntryM.objects.all().count()
    supplier=SupplierInfoM.objects.all().count()
    purchage=PurchageExtendM.objects.all().count()
    return render(request,'inventory/Dashboard.html',{'intem':intem,'supplier':supplier,'purchage':purchage})

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
    supplier=SupplierInfoM.objects.all()
    return render(request,'inventory/supplier.html',{'supplier':supplier})


def suppliernameSaveV(request):
    if request.method=='POST':
        name=request.POST.get('suppliername')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        email=request.POST.get('email')

        datasave=SupplierInfoM.objects.create(Suppliername=name,Address=address,Phone=phone,Email=email)
    return redirect('/supplier/entry/')

def suppliernameeditV(request,id=0):
    supplier=SupplierInfoM.objects.all()
    if id !=0:
        datasupply=SupplierInfoM.objects.filter(pk=id)
    return render(request, 'inventory/supplieredit.html',{'supplier':supplier,'datasupply':datasupply})

def suppliernameupdateV(request,id=0):
    if request.method=='POST':
        if id !=0:
            name = request.POST.get('suppliername')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            email = request.POST.get('email')

            dataupdate=SupplierInfoM.objects.get(pk=id)
            dataupdate.Suppliername=name
            dataupdate.Address=address
            dataupdate.Phone=phone
            dataupdate.Email=email
            dataupdate.save()
            messages.info(request,'Data Updated')
    return redirect('/supplier/entry/')

def suppliernamedeleteV(request, id=0):
    if id !=0:
        datadelete=SupplierInfoM.objects.get(pk=id)
        datadelete.delete()
        messages.info(request,'Data Delete')
    return redirect('/supplier/entry/')

def hrdashboardV(request):
    return render(request,'hr/dashboard.html')

def hrnameV(request):
    eidname=EmployeesInformationM.objects.raw('select id,count(Employees_id)+1 as eid from insurance_employeesinformationm')
    employeesinfo=EmployeesInformationM.objects.all()
    return render(request,'hr/Employees.html',{'eidname':eidname,'employeesinfo':employeesinfo})

def hrnameSaveV(request):
    if request.method=='POST':
        name=request.POST.get('name')
        designation=request.POST.get('designation')
        depertment=request.POST.get('depertment')
        eid=request.POST.get('eid')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        paddress=request.POST.get('paddress')
        peraddress=request.POST.get('peraddress')
        dates=request.POST.get('dates')

        if not dates:
            da=None
        else:
            da=datetime.datetime.strptime(dates, '%Y-%m-%d')

        datasave=EmployeesInformationM.objects.create(Name=name,Designation=designation,Depertment=depertment,
                                                      Employees_id=eid,Present_address=paddress,
                                                      Permanent_address=peraddress,Date_of_Birth=da,Phone=phone,
                                                      Email=email)
        messages.info(request, 'Data Save')
    return redirect('/hr/entry/')

def hrnameeditV(request,id=0):
    employeesinfo = EmployeesInformationM.objects.all()
    if id !=0:
        dataget=EmployeesInformationM.objects.filter(pk=id)
    return render(request,'hr/Employeesedit.html',{'dataget':dataget,'employeesinfo':employeesinfo})

def hrnameupdateV(request,id=0):
    employeesinfo = EmployeesInformationM.objects.all()
    if request.method=='POST':
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        depertment = request.POST.get('depertment')
        eid = request.POST.get('eid')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        paddress = request.POST.get('paddress')
        peraddress = request.POST.get('peraddress')
        dates = request.POST.get('dates')
        if not dates:
            da=None
        else:
            da=datetime.datetime.strptime(dates, '%Y-%m-%d')
        dataupdate=EmployeesInformationM.objects.get(pk=id)
        dataupdate.Employees_id=eid
        dataupdate.Name=name
        dataupdate.Designation=designation
        dataupdate.Depertmant=depertment
        dataupdate.Phone=phone
        dataupdate.Email=email
        dataupdate.Present_address=paddress
        dataupdate.Permanent_address=peraddress
        if not dates:
            dataupdate.Date_of_Birth=None
        else:
            dataupdate.Date_of_Birth=datetime.datetime.strptime(dates, '%Y-%m-%d')
        dataupdate.save()
        messages.info(request, 'Data Update')

    return redirect('/hr/entry/')

def hrnamedeleteV(request,id=0):
    if id !=0:
        datadelete=EmployeesInformationM.objects.get(pk=id)
        datadelete.delete()
        messages.info(request, 'Data Delete')
    return redirect('/hr/entry/')

def purchangeV(request):
    suplier=SupplierInfoM.objects.all()
    item=ItemEntryM.objects.all()
    inv=PurchageExtendM.objects.raw('select id,count(less)+1 as invs from insurance_purchageextendm')
    purx=PurchageExtendM.objects.filter(Invoice_no=3)
    p=PurchageInfoM.objects.raw('SELECT a.id,a.Item_name,a.Quantity,a.Rate,(a.Quantity*a.Rate) as Total from insurance_purchageinfom as a, insurance_purchageextendm as b'
                                ' where a.pex_id=b.id and Invoice_no=%s',[3])
    sumation=PurchageInfoM.objects.raw('SELECT a.id,sum(a.Quantity) as sumQuantity,sum(a.Quantity*a.Rate) as sTotal,sum(b.vat)as vat,sum(a.Quantity*a.Rate)-((sum(a.Quantity*a.Rate)*sum(b.vat))/100) as subtotal,sum(b.less) as less,sum(a.Quantity*a.Rate)-((sum(a.Quantity*a.Rate)*sum(b.vat))/100)- sum(b.less) as Grant_total from insurance_purchageinfom as a, insurance_purchageextendm as b'
                                        ' where a.pex_id=b.id and Invoice_no=%s',[3])



    return render(request,'inventory/purchage.html',{'suplier':suplier,'item':item,'inv':inv,'purx':purx,'p':p,'sumation':sumation})

def purchangeSaveV(request):
    if request.method=='POST':
        date=request.POST.get('date')
        d=datetime.datetime.strptime(date, '%Y-%m-%d')
        pno=request.POST.get('pno')
        sname=request.POST.get('sname')
        vat=request.POST.get('vat') or 0
        less=request.POST.get('less') or 0
        item=request.POST.getlist('item')
        qty=request.POST.getlist('qty')
        uprice=request.POST.getlist('uprice')
        supname=SupplierInfoM.objects.get(id=sname)

        datasave = PurchageExtendM(Pdate=d, Invoice_no=pno,Supplier_name=supname, Vat=vat, Less=less)
        datasave.save()
        da=PurchageExtendM.objects.get(pk=datasave.id)
        cd = min([len(item), len(qty), len(uprice)])
        for i in range(cd):
            data=PurchageInfoM(pex=da,Item_name=item[i],Quantity=qty[i],Rate=uprice[i])
            data.save()

        messages.info(request,'Data Save')
    return redirect('/purchange/entry/')



def PurchagePDFV(request):
    invoice=request.POST.get('invoiceno')
    purx = PurchageExtendM.objects.filter(Invoice_no=invoice)
    p = PurchageInfoM.objects.raw(
        'SELECT a.id,a.Item_name,a.Quantity,a.Rate,(a.Quantity*a.Rate) as Total from insurance_purchageinfom as a, insurance_purchageextendm as b'
        ' where a.pex_id=b.id and Invoice_no=%s', [invoice])
    sumation = PurchageInfoM.objects.raw(
        'SELECT a.id,sum(a.Quantity) as sumQuantity,sum(a.Quantity*a.Rate) as sTotal,b.vat as vat,(sum(a.Quantity*a.Rate)*(b.vat))/100 as vatamount,(sum(a.Quantity*a.Rate)-(sum(a.Quantity*a.Rate)*(b.vat))/100) as subtotal,b.less as less,(sum(a.Quantity*a.Rate)-((sum(a.Quantity*a.Rate)*(b.vat))/100)- b.less) as Grant_total from insurance_purchageinfom as a, insurance_purchageextendm as b'
        ' where a.pex_id=b.id and Invoice_no=%s', [invoice]
      )

    template_path = 'inventory/purchagepdf.html'
    context = {'purx':purx,'p':p,'sumation':sumation}
    response = HttpResponse(content_type='application/pdf')
    # for downlode
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


