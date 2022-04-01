from django.shortcuts import render,redirect
from .models import Atendimento, Responsavel, Pet
from .form import AtendimentoForm, PetForm, ResponsavelForm


def home(request):
     data = {}
     data['lista'] = ['t1', 't2', 't3']
     return render(request, 'atendimento/home.html', data)


def listagem(request):
    data = {}
    data['lista'] = Atendimento.objects.filter()
    return render(request, 'atendimento/lista.html', data)


def lista_pet(request):
    data = {}
    data['lista'] = Pet.objects.filter()
    return render(request, 'atendimento/lista_pets.html', data)


def lista_responsaveis(request):
    data = {}
    data['lista'] = Responsavel.objects.filter()
    return render(request, 'atendimento/lista_responsaveis.html', data)


def novo_atendimento(request):
    data = {}
    form = AtendimentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_lista')
    data['form'] = form
    return render(request, 'atendimento/atendimento_form.html', data)


def novo_pet(request):
    data = {}
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_lista')
    data['form'] = form
    return render(request, 'atendimento/pet_form.html', data)


def novo_responsavel(request):
    data = {}
    form = ResponsavelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_lista')
    data['form'] = form
    return render(request, 'atendimento/responsavel_form.html', data)


def atualizar(request, pk):
    data = {}
    atendimento = Atendimento.objects.get(pk=pk)
    form = AtendimentoForm(request.POST or None, instance=atendimento)

    if form.is_valid():
        form.save()
        return redirect('url_lista')

    data['form'] = form
    data['atendimento'] = atendimento
    return render(request, 'atendimento/atendimento_form.html', data)


def atualizar_responsavel(request, pk):
    data = {}
    responsavel = Responsavel.objects.get(pk=pk)
    form = ResponsavelForm(request.POST or None, instance=responsavel)

    if form.is_valid():
        form.save()
        return redirect('url_lista_responsavel')

    data['form'] = form
    data['responsavel'] = responsavel
    return render(request, 'atendimento/responsavel_form.html', data)


def atualizar_pet(request, pk):
    data = {}
    pet = Pet.objects.get(pk=pk)
    form = PetForm(request.POST or None, instance=pet)

    if form.is_valid():
        form.save()
        return redirect('url_lista_pet')

    data['form'] = form
    data['pet'] = pet
    return render(request, 'atendimento/pet_form.html', data)


def delete(request, pk):
    atendimento = Atendimento.objects.get(pk=pk)
    atendimento.delete()
    return redirect('url_lista')


def deletePet(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.delete()
    return redirect('url_lista_pet')


def deleteResponsavel(request, pk):
    responsavel = Responsavel.objects.get(pk=pk)
    responsavel.delete()
    return redirect('url_lista_responsavel')