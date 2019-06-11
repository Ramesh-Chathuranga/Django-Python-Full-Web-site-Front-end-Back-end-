from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import Company,Employee
from .form import UserForm



class IndexView(generic.ListView):
    template_name='miriapp/index.html'
    context_object_name = 'company_list'
    def get_queryset(self):
        return Company.objects.all()

class DetailView(generic.DetailView):
    model = Company
    template_name = 'miriapp/detail.html'


class CompanyCreate(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Company
    fields = ['name','logo','website','email']



class CompanyUpdate(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Company
    fields = ['name', 'logo', 'website', 'email']

class CompanyDelete(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Company
    success_url = reverse_lazy('index')

class UserFormView(View):
    from_class=UserForm
    template_name = 'miriapp/registration_form.html'

    def get(self,request):
        form = self.from_class(None)
        return  render(request,self.template_name,{'form':form})

    def post(self,request):
       form=self.form_class(request.POST)

       if form.is_valid():
           user = form.save(comit=False)

           username = form.cleaned_data['username']
           password = form.cleaned_data['password']
           user.set_password(password)
           user.save()

           user = authenticate(username=username,password=password)

           if user is not None:
               if user.is_active:
                   login(request,user)
                   return redirect('index')
       return render(request, self.template_name, {'form': form})


class EmployeeCreate(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Employee
    fields = ['company', 'first_name', 'last_name', 'phone','email']


class EmployeeUpdate(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Employee
    fields = ['company', 'first_name', 'last_name','phone', 'email']


class EmployeeDelete(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Employee
    success_url = reverse_lazy('index')


class UserLogOut():
    def logout_view(request):
        logout(request)
        return redirect('login')
