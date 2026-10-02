from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Paciente

# Create your views here.
@login_required
def index(request):
    if request.method == "POST":
        Paciente.objects.create(
            nome=request.POST.get("nome"),
            cpf=request.POST.get("cpf"),
            email=request.POST.get("email"),
            telefone=request.POST.get("telefone"),
            data_nascimento=request.POST.get("data_nascimento"),
        )

        return redirect("index")

    return render(request, "novo-paciente.html")
