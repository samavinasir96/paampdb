from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Q
from django.views.generic import ListView, TemplateView, FormView
from .models import PDBQuery, AMP, TargetProtein, Dock
import os

def EnterPage(request):
    return render(request, "search.html")

def IndexPage(request):
    return render(request, "index.html")

def AboutUsPage(request):
    return render(request, "about_us.html")

def StatsPage(request):
    return render(request, "stats.html")

class ContactView(generic.TemplateView):
    """Contact section of the AMPdb tool."""
    model = PDBQuery
    template_name = "contact.html"

def TutorialPage(request):
    return render(request, 'tutorial.html')

def search_view(request):
    return render(request, "search.html", {
        "targets": TargetProtein.objects.all(),
        "proteins": AMP.objects.all()
    })

def protein(request, proteins_id):
    protein = get_object_or_404(AMP, pk=proteins_id)
    target_protein = protein.target_protein
    dock = Dock.objects.filter(amp=protein, target_protein=target_protein)
    return render(request, "protein.html", {
        "protein": protein,
        "dock": dock,
    })


def create_protein(request):
    if request.method == 'POST':
        protein_id = request.POST.get('protein_id')
        protein_name = request.POST.get('protein_name')
        score = request.POST.get('score')
        sequence = request.POST.get('sequence')
        target_protein_id = request.POST.get('target_id')
        
        try:
            protein = AMP.objects.get(id=protein_id)
            protein.target_protein_id = target_protein_id
            protein.save()
            
            target_protein = TargetProtein.objects.get(id=target_protein_id)
            target_protein_name = target_protein.target_protein + '_' + protein.pdb_name[2:]
            
            dock_instances = Dock.objects.filter(dock__contains=target_protein_name)
            for dock_instance in dock_instances:
                dock_instance.target_protein.add(target_protein)
            
            redirect_url = reverse('protein', kwargs={'proteins_id': protein_id})
            return redirect(redirect_url)
        except AMP.DoesNotExist:
            messages.error(request, 'Protein not found')
            return redirect('create_protein')  # Redirect to a relevant page
        except TargetProtein.DoesNotExist:
            messages.error(request, 'Target Protein not found')
            return redirect('create_protein')  # Redirect to a relevant page
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return redirect('create_protein')  # Redirect to a relevant page
    else:
        return HttpResponse('Invalid request method')

