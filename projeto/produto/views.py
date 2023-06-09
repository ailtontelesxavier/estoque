from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import CreateView, UpdateView, DeleteView
from produto.models import Produto
from produto.forms import ProdutoForm


def produto_list(request):
    template_name = 'produto_list.html'
    objects = Produto.objects.all()
    context = {'object_list': objects}
    
    return render(request, template_name, context)


def produto_detail(request, pk):
    template_name = 'produto_detail.html'
    obj = Produto.objects.get(pk=pk)
    context = {'object': obj}
    
    return render(request, template_name, context)


def produto_add(request):
    template_name = 'produto_form.html'
    
    return render(request, template_name)


class ProdutoCreate(CreateView):
    template_name = 'produto_form.html'
    model = Produto
    form_class = ProdutoForm
    

class ProdutoUpdate(UpdateView):
    template_name = 'produto_form.html'
    model = Produto
    form_class = ProdutoForm
    
    
def produto_json(request, pk):
    produto = Produto.objects.filter(pk=pk)
    data = [item.to_dict_json() for item in produto]
    
    return JsonResponse({'data':data})