from django.urls import path,include
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import routers
from django.conf.urls import url
# from django.contrib import auth
# from django.contrib.auth import login, authenticate
# from .views import home


# router = routers.DefaultRouter()
# router.register('api', views.SuperadminList)
urlpatterns = [
    # path('', views.home, name='home'),
    # url(r'^login/$', views.login, name='login'),
    # url(r'^logout/$', views.logout, name='logout'),
    # url(r'^google_auth/', include('google_auth.urls')),  # <- Here
    # url(r'^$', home, name='home'),
    # url(r'^auth/', include('social_django.urls', namespace='social')),
    # url('', include('django_oauth2.urls', namespace='social')),
    path('api/token/', views.TokenList.as_view()),
    path('api/subadmin/', views.SubadminList.as_view()),
    path('api/subadmin/<int:pk>/', views.SubadminDetail.as_view()),
    path('api/borrower/', views.BorrowerList.as_view()),
    path('api/borrower/<int:pk>/', views.BorrowerDetail.as_view()),
    # path('api/home/', views.home),
    # path('api/logout/', views.logout),
    #FACILITIES PATH
    path('api/facilityss/', views.FacilityListss.as_view()),
    path('api/facilityss/<int:pk>', views.FacilityDetailss.as_view()),
    path('api/facility/', views.FacilityList),
    path('api/available/', views.Facilityavailable),
    path('api/unavailable/', views.FacilityUnavailable),
    path('api/status0/<int:pk>', views.Facilitystatus0, name='Facilitystatus0'),
    path('api/status1/<int:pk>', views.Facilitystatus1, name='Facilitystatus1'),
    path('api/quantity/', views.Facilityquantity),
    path('api/edit/<int:pk>', views.FacilityEdit, name='FacilityEdit'),

    #EQUIPMENT PATH
    path('api/equipment/', views.EquipmentList),
    path('api/Eavailable/', views.Equipmentavailable),
    path('api/Eunavailable/', views.EquipmentUnavailable),
    path('api/Estatus0/', views.Equipmentstatus0),
    path('api/Estatus1/', views.Equipmentstatus1),
    path('api/Equantity/', views.Equipmentquantity),
    path('api/Eedit/', views.EquipmentEdit),
    # path('api/equipment/<int:pk>/', views.EquipmentDetail
]

# urlpatterns = format_suffix_patterns(urlpatterns)