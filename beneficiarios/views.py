from django.shortcuts import render
from django.views import generic
from .models import Beneficiarios, Cargo, Gerencia
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
import re


def DeleteBeneficiario(request, pk):
    Beneficiarios.objects.filter(pk=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    """
    try:
        b = Beneficiarios.objects.get(cedula=pk)
    except Beneficiarios.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'No existe el beneficiario')
        return redirect('beneficiarios')
    b.status = 0
    b.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    """

class BeneficiariosListView(generic.ListView):
    model = Beneficiarios
    template_name = 'sections/beneficiarios/index.html'  # Specify your own template name/location


class BeneficiariosCreateView(generic.CreateView):
    template_name = "sections/beneficiarios/crear.html"

    def get(self, request, *args, **kwargs):
        c = Cargo.objects.all().order_by('nombre')
        g = Gerencia.objects.all()
        context = {
            'cargo':c,
            'gerencias':g
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        cedula = request.POST.get('cedula')
        nombres = request.POST.get('nombres')
        cargo = request.POST.get('cargo')
        status = request.POST.get('status')
        gerencia = request.POST.get('gerencia')

        if validcedula(cedula) != True:
            messages.add_message(request, messages.ERROR, 'La cedula no es valida')
            return redirect('beneficiarios_crear')

        if len(nombres) < 2:
            messages.add_message(request, messages.ERROR, 'El nombre no es valido debe ser mayor a 2 digitos al menos')
            return redirect('beneficiarios_crear')

        if cargo == '--------------------------':
            messages.add_message(request, messages.ERROR, 'El cargo no es valido')
            return redirect('beneficiarios_crear')

        if Beneficiarios.objects.filter(cedula=cedula).exists():
            messages.add_message(request, messages.ERROR, 'El beneficiario ingresado ya se encuentra registrado.')
            return render(request, self.template_name)
        else:
            gerencia = Gerencia.objects.get(pk=gerencia)
            b = Beneficiarios(cedula=cedula, nombres=nombres, cargo=cargo, status=status, gerencia=gerencia)
            b.save()

        messages.add_message(request, messages.SUCCESS, 'Beneficiario creado con exito')
        return redirect('beneficiarios')

class BeneficiariosUpdateView(generic.View):
    template_name = "sections/beneficiarios/edit.html"

    def get(self, request, *args, **kwargs):
        cargos = Cargo.objects.all().order_by('nombre')
        beneficiarios = Beneficiarios.objects.get(cedula=kwargs['pk'])
        gerencias = Gerencia.objects.all()

        context = {
            'cargo': cargos, 
            'beneficiario': beneficiarios,
            'gerencias':gerencias
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        cedula = request.POST.get('cedula')
        nombres = request.POST.get('nombres')
        cargo = request.POST.get('cargo')
        status = request.POST.get('status')
        gerencia = request.POST.get('gerencia')
        observacion = request.POST.get('observacion')

        try:
            b = Beneficiarios.objects.get(cedula=cedula)
        except Beneficiarios.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'No existe el beneficiario')
            return redirect('beneficiarios')
        
        if validcedula(cedula) != True:
            messages.add_message(request, messages.ERROR, 'La cedula no es valida')
            return redirect('beneficiarios_editar', pk=cedula)

        if len(nombres) < 2:
            messages.add_message(request, messages.ERROR, 'El nombre no es valido debe ser mayor a 2 digitos al menos')
            return redirect('beneficiarios_editar', pk=cedula)

        if cargo == '--------------------------':
            messages.add_message(request, messages.ERROR, 'El cargo no es valido')
            return redirect('beneficiarios_editar', pk=cedula)
        
        g = Gerencia.objects.get(pk=gerencia)

        b.cedula = cedula
        b.nombres = nombres
        b.cargo = cargo
        b.status = status
        b.gerencia = g
        b.observacion = observacion
        b.save()

        messages.add_message(request, messages.SUCCESS, 'Beneficiario editado con exito')
        return redirect('beneficiarios')

def validcedula(cedula):
    if (re.match('\d', cedula) and (len(cedula) == 8 or len(cedula)== 7)):
        return True
    else:
        return False
        

class BeneficiarioDeleteView(generic.DeleteView):
    template_name = "sections/beneficiarios/delete.html"
    def get(self, request, *args, **kwargs):
        beneficiario = Beneficiarios.objects.get(pk=kwargs['pk'])
        context = {
            'beneficiario': beneficiario
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        observacion = request.POST.get('observacion')
        try:
            b = Beneficiarios.objects.get(cedula=kwargs['pk'])
        except Beneficiarios.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'No existe el beneficiario')
            return redirect('beneficiarios')
        b.status = 0
        b.observacion = observacion
        b.save()
        messages.add_message(request, messages.SUCCESS, 'Beneficiario deshabilitado')
        return redirect('beneficiarios')


class BeneficiarioDetailView(generic.View):
    template_name = "sections/beneficiarios/detail.html"

    def get(self, request, *args, **kwargs):
        beneficiario = Beneficiarios.objects.get(pk=kwargs['pk'])
        context = {
            'beneficiario':beneficiario
        }
        return render(request, self.template_name, context)