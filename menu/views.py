from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ItemForm
from .models import Item
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

# Create your views here.



class IndexClassView(ListView):
    model = Item;
    template_name = 'menu/index.html'
    context_object_name = 'item_list'

def items(request):
    return HttpResponse('Widok pozycji menu')

def start(request):
    return render(request, 'menu/start.html')



class FoodDetail(DetailView):
    model = Item;
    template_name = 'menu/detail.html'


def create_item(request):

        form = ItemForm(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect('menu:index')

        return render(request, 'menu/item-form.html', {'form':form})

class CreateItem(LoginRequiredMixin ,CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_img']
    template_name = 'menu/item-form.html'


    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)


def edit_item(request, id):
    item = Item.objects.get(id=id)
    form =  ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('menu:index')
    return render(request, 'menu/item-form.html', {'form':form, 'item':item})

def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('menu:index')

    return render(request, 'menu/item-delete.html', {'item':item})


