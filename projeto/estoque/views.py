from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.forms import inlineformset_factory
from estoque.models import Estoque, EstoqueItens
from estoque.forms import EstoqueForm, EstoqueItensForm


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


def estoque_entrada_add(request):
    templa_name = 'estoque_entrada_form.html'
    estoque_form = Estoque()
    item_estoque_formset = inlineformset_factory(
        Estoque,
        EstoqueItens,
        form = EstoqueItensForm,
        extra = 0,
        min_num = 1,
        validate_min = True,
    )
    
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque_form, prefix='main')
        formset = item_estoque_formset(
            request.POST,
            instance=estoque_form, 
            prefix='estoque'
            )
        if form.is_valid() and formset.is_valid():
            form = form.save()
            formset.save()
            url = 'estoque:estoque_entrada_detail'
            
            return HttpResponseRedirect(resolve_url(url, form.pk))
    else:
        form = EstoqueForm(instance=estoque_form, prefix='main')
        formset = item_estoque_formset(instance=estoque_form, prefix='estoque')
    
    context = {
        'form': form,
        'formset': formset,
    }
    
    return render(request, templa_name, context,)