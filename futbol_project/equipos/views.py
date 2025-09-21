from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from django.contrib.auth import authenticate, login

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('inicio')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})
