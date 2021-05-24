from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.mainV,name='main'),
    path('', views.indexV,name='index'),
    path('login/', views.logingV,name='login'),
    path('logout/', views.loguotV,name='logout'),
    path('dashboard/', views.DashboardV,name='Dashboard'),
    path('admin/dashboard/', views.admindashboardV,name='admindashboard'),
    path('inventory/dashboard/', views.inventorydashboardV,name='inventorydashboard'),
    path('hr/dashboard/', views.hrdashboardV,name='hrdashboard'),
    path('create/user/', views.createuserV,name='createuser'),
    ############ Item Information #############################
    path('item/entry/', views.itemnameV,name='itementry'),
    path('item/entry/save/', views.itemnameSaveV,name='itementrysave'),
    path('item/entry/edit/<int:id>/', views.itemnameeditV,name='itementryedit'),
    path('item/entry/update/<int:id>/', views.itemnameupdateV,name='itementryupdate'),
    path('item/entry/delete/<int:id>/', views.itemnamedeleteV,name='itementrydelete'),
    ############ Item Information #############################
    path('supplier/entry/', views.suppliernameV,name='supplierentry'),
    path('supplier/entry/save/', views.suppliernameSaveV,name='supplierentrysave'),
    path('supplier/entry/edit/<int:id>/', views.suppliernameeditV,name='supplierentryedit'),
    path('supplier/entry/update/<int:id>/', views.suppliernameupdateV,name='supplierentryupdate'),
    path('supplier/entry/delete/<int:id>/', views.suppliernamedeleteV,name='supplierentrydelete'),
    ############ HR Information #############################
    path('hr/entry/', views.hrnameV, name='hrrentry'),
    path('hr/entry/save/', views.hrnameSaveV, name='hrentrysave'),
    path('hr/entry/edit/<int:id>/', views.hrnameeditV, name='hrentryedit'),
    path('hr/entry/update/<int:id>/', views.hrnameupdateV, name='hrentryupdate'),
    path('hr/entry/delete/<int:id>/', views.hrnamedeleteV, name='hrentrydelete'),
    ############ purchage Information #############################
    path('purchange/entry/', views.purchangeV, name='purchangeentry'),
    path('purchange/entry/save/', views.purchangeSaveV, name='purchangeentrysave'),
    path('purchange/entry/edit/', views.purchangeEditV, name='purchangeEdit'),
    path('purchange/entry/edit/item/', views.purchangeEdititemV, name='purchangeEdititem'),
    path('purchange/entry/update/', views.purchangeupdateV, name='purchangeupdate'),
    # path('hr/entry/delete/<int:id>/', views.hrnamedeleteV, name='hrentrydelete'),
    path('Purchage/PDF/', views.PurchagePDFV, name='purchagepdf'),


    # ############ issue Information #############################
    # path('purchange/entry/', views.purchangeV, name='purchangeentry'),
    # path('purchange/entry/save/', views.purchangeSaveV, name='purchangeentrysave'),
    # # path('hr/entry/edit/<int:id>/', views.hrnameeditV, name='hrentryedit'),
    # # path('hr/entry/update/<int:id>/', views.hrnameupdateV, name='hrentryupdate'),
    # # path('hr/entry/delete/<int:id>/', views.hrnamedeleteV, name='hrentrydelete'),
    # path('Purchage/PDF/', views.PurchagePDFV, name='purchagepdf'),





























]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
