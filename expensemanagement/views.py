from django.shortcuts import render,redirect
from django.views.generic import View
from expensemanagement.forms import SigninForm,RegisterForm,ExpenseAddForm,ExpenseManagement
from django.contrib.auth import authenticate,login,logout

class SignUpView(View):

    form_class=SigninForm

    template_name="signup.html"

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            form_instance.save()

            print("your session start")

            return redirect("signup")
        
        print("faild")

        return render(request,self.template_name,{"form":form_instance})

class SignInView(View):

    form_class=RegisterForm

    template_name="signin.html"

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            uname=data.get("username")

            pwd=data.get("password")

            user_object=authenticate(request,username=uname,password=pwd)

            if user_object:

                login(request,user_object)

                print("your session start")

                return redirect("expense-list")
            
            print("invaliad")

            return render(request,self.template_name,{"form":form_instance})

class ExpenseAddView(View):

    form_class=ExpenseAddForm

    template_name="expenseadd.html"

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data,files=request.FILES)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            ExpenseManagement.objects.create(**data)

            return redirect("expense-add")
        
        return render(request,self.template_name,{"form":form_instance})
    
class ExpenseListView(View):

    template_name="expense.html"

    def get(self,request,*args,**kwargs):

        qs=ExpenseManagement.objects.all()

        return render(request,self.template_name,{"data":qs})

class ExpenseDetailView(View):

    template_name="expense_detail.html"

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=ExpenseManagement.objects.get(id=id)
    
        return render(request,self.template_name,{"data":qs})
    
class ExpenseUpdateView(View):

    form_class=ExpenseAddForm

    template_name="expense_update.html"

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        expense_object=ExpenseManagement.objects.get(id=id)

        form_instance=self.form_class(instance=expense_object)

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        expense_object=ExpenseManagement.objects.get(id=id)

        form_data=request.POST

        form_instance=self.form_class(form_data,files=request.FILES,instance=expense_object)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("expense-list")
        
        return render(request,self.template_name,{"form":form_instance})
    
class ExpenseDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        ExpenseManagement.objects.get(id=id).delete()

        return redirect("expense-list")