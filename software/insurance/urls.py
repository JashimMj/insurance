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




























]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
