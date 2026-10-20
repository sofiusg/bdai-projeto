from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Luthier, Guitar
from .forms import LuthierForm, GuitarForm

# Create your views here.

from django.shortcuts import render
from .models import Luthier
def luthiersHTMLFUNC(request):
    return render(request, 'luthiersHTML.html', {})
def luthiersTESTEFUNC(request):
    luthiers = Luthier.objects.all()
    return render(request, 'luthiersTESTE.html', {'luthiers': luthiers})

# Home
class HomeView(TemplateView):
    template_name = "home.html"

# Luthiers
class LuthierListView(ListView):
    model = Luthier
    template_name = "luthier_list.html"
    context_object_name = "luthiers"

class LuthierDetailView(DetailView):
    model = Luthier
    template_name = "luthier_detail.html"
    context_object_name = "luthier"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["guitarras"] = self.object.guitarras.all()
        return context

class LuthierCreateView(CreateView):
    model = Luthier
    form_class = LuthierForm
    template_name = "luthier_form.html"
    success_url = reverse_lazy("luthier_list")

class LuthierUpdateView(UpdateView):
    model = Luthier
    form_class = LuthierForm
    template_name = "luthier_form.html"
    success_url = reverse_lazy("luthier_list")

class LuthierDeleteView(DeleteView):
    model = Luthier
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("luthier_list")

# Guitarras

class GuitarListView(ListView):
    model = Guitar
    template_name = "guitar_list.html"
    context_object_name = "guitarras"
    queryset = Guitar.objects.select_related("luthier").all()

class GuitarDetailView(DetailView):
    model = Guitar
    template_name = "guitar_detail.html"
    context_object_name = "guitar"

class GuitarCreateView(CreateView):
    model = Guitar
    form_class = GuitarForm
    template_name = "guitar_form.html"
    success_url = reverse_lazy("guitar_list")

class GuitarUpdateView(UpdateView):
    model = Guitar
    form_class = GuitarForm
    template_name = "guitar_form.html"
    success_url = reverse_lazy("guitar_list")

class GuitarDeleteView(DeleteView):
    model = Guitar
    template_name = "confirm_deleteGUITAR.html"
    success_url = reverse_lazy("guitar_list")
