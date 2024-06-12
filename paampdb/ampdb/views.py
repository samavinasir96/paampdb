from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import PDBQuery


class IndexView(generic.ListView):
    template_name = "abampdb/index.html"

    def get_queryset(self):
        return PDBQuery.objects.all()


class DetailView(generic.DetailView):
    model = PDBQuery
    template_name = "abampdb/results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["system"] = self.request.GET.get("system", None)
        return context

    # def search(self):
    #     if request.method == 'GET':
    #     try:
    #         query = PDBQuery.objects.get(name = query_id)
    #         if query_id == search_id:
    #             return get_object_or_404(html)
    #     except PDBQuery.DoesNotExist:
    #         return HttpResponse("no such protein available")
    # else:
    #     return render(request, 'abampdb/index.html')
