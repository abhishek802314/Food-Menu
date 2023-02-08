from django.shortcuts import render, HttpResponse, redirect
from .models import Item
from .forms import ItemForm
from django.views.generic.edit import CreateView
# Create your views here.

def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list':item_list
    }
    return render(request, 'index.html', context)

def items(request):
    return HttpResponse("This is item")


def detail(request, pk):
    item = Item.objects.get(id= pk)
    context = {
        'item':item
    }
    return render(request, 'detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)
    context={'form':form}

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'item-form.html', context)

#this is a class based view for create item
class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'item-form.html'
    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)



def update_item(request, pk):
    item = Item.objects.get(id=pk)
    form = ItemForm(request.POST or None, instance=item)
    context = {'form':form, 'item':item}
    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'item-form.html', context )

def delete_item(request, pk):
    item = Item.objects.get(id=pk)
    context = {'item':item}
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request, 'item-delete.html', context)