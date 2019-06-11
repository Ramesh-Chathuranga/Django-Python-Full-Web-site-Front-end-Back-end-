from django.conf.urls import url
from . import views

urlpatterns = [
    # save Employee
    url(r'^add/$', views.EmployeeCreate.as_view(), name='employee-add'),
    # select Employee to update
    url(r'^update/(?P<pk>[0-9]+)/$', views.EmployeeUpdate.as_view(), name='employee-update'),
    # delete Employee
    url(r'^(?P<pk>[0-9]+)/delete/$', views.EmployeeDelete.as_view(), name='employee-delete'),
]