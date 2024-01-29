from django.shortcuts import render, redirect
from django.http import HttpResponse
from food.models import Item
from food.form import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


# Create your views her
#function based index view
#---------------------------------------------------------------
def index(request):
    itemlist = Item.objects.all()

    context={
        'itemlist':itemlist
    }
    return render(request, 'food/home.html',context)

#class based index view
#---------------------------------------------------------------
class IndexClassView(ListView):
    model = Item
    context_object_name = 'itemlist'
    template_name = 'food/home.html'

#function based detail view
#---------------------------------------------------------------
def detail(request,item_id):
    item= Item.objects.get(id= item_id)

    context={"item":item}
    return render(request,"food/detail.html",context)

#class based detail view
#---------------------------------------------------------------
class FoodDetail(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = "food/detail.html"


#function based create item view
#---------------------------------------------------------------
def CreateItem(request):

    form = ItemForm(request.POST or None)
    if request.method == 'POST':
        form.instance.added_by = request.user.username
        form.save()
        return redirect('food:index')

    context = {
        'form':form
    }
    
    return render(request, 'food/item-form.html', context)

#class based create item view
#---------------------------------------------------------------
class CreateItem(CreateView):
    model = Item
    fields = ['rest_owner','prod_code','item_name','item_desc','item_price','item_image']
    template_name = 'food/item-form.html'
    context_object_name = 'form'
    success_url = reverse_lazy('food:index')

    def form_valid(self,form):
         form.instance.added_by = self.request.user.username
         return super().form_valid(form )


#function based update item view
#---------------------------------------------------------------
def UpdateItem(request,item_id):

    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:detail', item_id)

    context ={
        'form':form
}

    return render(request,'food/item-form.html',context)


#function based delete item view
#---------------------------------------------------------------
def DeleteItem(request, item_id):

    item = Item.objects.get(id=item_id)

    context ={
        'item':item
    }

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request,'food/item-delete.html',context)
