from django.conf.urls import url
from . import views

urlpatterns = [
    #homepage
       url(r'^$', views.IndexView.as_view() , name='index'),
    #select company
       url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #save Company
       url(r'^add/$', views.CompanyCreate.as_view(), name='company-add'),
    # select company to update
       url(r'^update/(?P<pk>[0-9]+)/$', views.CompanyUpdate.as_view(), name='company-update'),
   #delete company
       url(r'^(?P<pk>[0-9]+)/delete/$', views.CompanyDelete.as_view(), name='company-delete'),
    # #register user
    #    url(r'^registers/$', views.UserFormView.as_view() , name='user-register'),



]
