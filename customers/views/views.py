from django.shortcuts import render, get_object_or_404, redirect
from customers.models import Customer
from django.db.models import Q
from customers.forms import CustomerForm
from django.core.paginator import Paginator
from django.views import View


class CustomerListView(View):
    def get(self, request):
        search = request.GET.get('q')
        order = request.GET.get('order', 'recent')

        customers = Customer.objects.all()

        if search:
            customers = customers.filter(
                Q(first_name__icontains=search) | Q(second_name__icontains=search) | Q(email__icontains=search)
            )

        if order == 'recent':
            customers = customers.order_by('-id')
        else:
            customers = customers.all()

        paginator = Paginator(customers, 2)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            'customers': customers,
            'customer_page': page_obj,
        }
        return render(request, 'customers/customers.html', context)



class CustomerDetailView(View):
    def get(self, request, customer_id):
        customer = get_object_or_404(Customer, id=customer_id)
        form = CustomerForm(instance=customer)
        context = {
            'form': form,
            'customer': customer,
        }
        return render(request, 'customers/customers-detail.html', context)

    def post(self, request, customer_id):
        customer = get_object_or_404(Customer, id=customer_id)
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail', customer_id=customer.id)
        context = {
            'form': form,
            'customer': customer,
        }
        return render(request, 'customers/customers-detail.html', context)




class CustomerCreateView(View):

    def get(self, request):
        form = CustomerForm()
        contex = {
            'form':form
        }
        return render(request, 'customers/add-customer.html', contex)

    def post(self, request):
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customer_list')



class CustomerUpdateView(View):

    def get(self, request, customer_id):
        customer = get_object_or_404(Customer, id=customer_id)
        form = CustomerForm(instance=customer)
        return render(request, 'customers/edit-customer.html', {'form':form, 'customer': customer})

    def post(self, request, customer_id):
        customer = get_object_or_404(Customer, id=customer_id)
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail', customer_id)



class CustomerDeleteView(View):
    def post(self, request, customer_id):
        customer = get_object_or_404(Customer, id=customer_id)
        if customer:
            customer.delete()
        return redirect('customer_list')

    def get(self, request, customer_id):
        customer = get_object_or_404(Customer, id=customer_id)
        context = {'customer': customer}
        return render(request, 'customers/delete-customer.html', context)
