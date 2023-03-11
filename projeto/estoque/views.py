from django.shortcuts import render
from estoque.models import Estoque


def estoque_entrada_list(request):
    templa_name = 'estoque_entrada_list.html'
    objects = Estoque.objects.filter(movimento='e')
    context = {'object_list': objects}
    
    return render(request, templa_name, context)


def estoque_entrada_detail(request, pk):
    templa_name = 'estoque_entrada_detail.html'
    obj = Estoque.objects.get(pk=pk)
    context = {'object': obj}
    
    return render(request, templa_name, context)
