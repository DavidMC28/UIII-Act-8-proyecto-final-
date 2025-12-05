from django.shortcuts import render, redirect
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import (
    PadreMadre, Nino, PersonalGuarderia, GrupoNinos, 
    ActividadGuarderia, AsistenciaNino, PagoMensualidad
)
from .forms import (
    PadreMadreForm, NinoForm, PersonalGuarderiaForm, GrupoNinosForm, 
    ActividadGuarderiaForm, AsistenciaForm, PagoForm
)

# Dashboard
def dashboard(request):
    num_ninos = Nino.objects.count()
    num_grupos = GrupoNinos.objects.count()
    num_personal = PersonalGuarderia.objects.count()
    
    context = {
        'page_title': 'Dashboard',
        'num_ninos': num_ninos,
        'num_grupos': num_grupos,
        'num_personal': num_personal
    }
    return render(request, 'app_guarderia/dashboard.html', context)

# CRUD Views for PadreMadre
class PadreMadreListView(ListView):
    model = PadreMadre
    template_name = 'app_guarderia/padre_madre/list.html'
    context_object_name = 'object_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Padres/Madres'
        return context

class PadreMadreDetailView(DetailView):
    model = PadreMadre
    template_name = 'app_guarderia/padre_madre/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Detalle de {self.object.nombre}'
        return context

class PadreMadreCreateView(CreateView):
    model = PadreMadre
    form_class = PadreMadreForm
    template_name = 'app_guarderia/padre_madre/form.html'
    success_url = reverse_lazy('padre_madre_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Nuevo Padre/Madre'
        return context

class PadreMadreUpdateView(UpdateView):
    model = PadreMadre
    form_class = PadreMadreForm
    template_name = 'app_guarderia/padre_madre/form.html'
    success_url = reverse_lazy('padre_madre_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Editar {self.object.nombre}'
        return context

class PadreMadreDeleteView(DeleteView):
    model = PadreMadre
    template_name = 'app_guarderia/padre_madre/delete.html'
    success_url = reverse_lazy('padre_madre_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Eliminar {self.object.nombre}'
        return context

# CRUD Views for Nino
class NinoListView(ListView):
    model = Nino
    template_name = 'app_guarderia/nino/list.html'
    context_object_name = 'object_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Niños'
        return context

class NinoDetailView(DetailView):
    model = Nino
    template_name = 'app_guarderia/nino/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Detalle de {self.object.nombre}'
        return context

class NinoCreateView(CreateView):
    model = Nino
    form_class = NinoForm
    template_name = 'app_guarderia/nino/form.html'
    success_url = reverse_lazy('nino_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Nuevo Niño'
        return context

class NinoUpdateView(UpdateView):
    model = Nino
    form_class = NinoForm
    template_name = 'app_guarderia/nino/form.html'
    success_url = reverse_lazy('nino_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Editar {self.object.nombre}'
        return context

class NinoDeleteView(DeleteView):
    model = Nino
    template_name = 'app_guarderia/nino/delete.html'
    success_url = reverse_lazy('nino_list')

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Http404:
            return redirect('nino_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Eliminar {self.object.nombre}'
        return context

# CRUD Views for PersonalGuarderia
class PersonalGuarderiaListView(ListView):
    model = PersonalGuarderia
    template_name = 'app_guarderia/personal_guarderia/list.html'
    context_object_name = 'object_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Personal de Guardería'
        return context

class PersonalGuarderiaDetailView(DetailView):
    model = PersonalGuarderia
    template_name = 'app_guarderia/personal_guarderia/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Detalle de {self.object.nombre}'
        return context

class PersonalGuarderiaCreateView(CreateView):
    model = PersonalGuarderia
    form_class = PersonalGuarderiaForm
    template_name = 'app_guarderia/personal_guarderia/form.html'
    success_url = reverse_lazy('personal_guarderia_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Nuevo Personal'
        return context

class PersonalGuarderiaUpdateView(UpdateView):
    model = PersonalGuarderia
    form_class = PersonalGuarderiaForm
    template_name = 'app_guarderia/personal_guarderia/form.html'
    success_url = reverse_lazy('personal_guarderia_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Editar {self.object.nombre}'
        return context

class PersonalGuarderiaDeleteView(DeleteView):
    model = PersonalGuarderia
    template_name = 'app_guarderia/personal_guarderia/delete.html'
    success_url = reverse_lazy('personal_guarderia_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Eliminar {self.object.nombre}'
        return context

# CRUD Views for GrupoNinos
class GrupoNinosListView(ListView):
    model = GrupoNinos
    template_name = 'app_guarderia/grupo_ninos/list.html'
    context_object_name = 'object_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Grupos de Niños'
        return context

class GrupoNinosDetailView(DetailView):
    model = GrupoNinos
    template_name = 'app_guarderia/grupo_ninos/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Detalle de {self.object.nombre_grupo}'
        return context

class GrupoNinosCreateView(CreateView):
    model = GrupoNinos
    form_class = GrupoNinosForm
    template_name = 'app_guarderia/grupo_ninos/form.html'
    success_url = reverse_lazy('grupo_ninos_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Nuevo Grupo'
        return context

class GrupoNinosUpdateView(UpdateView):
    model = GrupoNinos
    form_class = GrupoNinosForm
    template_name = 'app_guarderia/grupo_ninos/form.html'
    success_url = reverse_lazy('grupo_ninos_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Editar {self.object.nombre_grupo}'
        return context

class GrupoNinosDeleteView(DeleteView):
    model = GrupoNinos
    template_name = 'app_guarderia/grupo_ninos/delete.html'
    success_url = reverse_lazy('grupo_ninos_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Eliminar {self.object.nombre_grupo}'
        return context

# CRUD Views for ActividadGuarderia
class ActividadGuarderiaListView(ListView):
    model = ActividadGuarderia
    template_name = 'app_guarderia/actividad_guarderia/list.html'
    context_object_name = 'object_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Actividades de la Guardería'
        return context

class ActividadGuarderiaDetailView(DetailView):
    model = ActividadGuarderia
    template_name = 'app_guarderia/actividad_guarderia/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Detalle de {self.object.nombre_actividad}'
        return context

class ActividadGuarderiaCreateView(CreateView):
    model = ActividadGuarderia
    form_class = ActividadGuarderiaForm
    template_name = 'app_guarderia/actividad_guarderia/form.html'
    success_url = reverse_lazy('actividad_guarderia_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Nueva Actividad'
        return context

class ActividadGuarderiaUpdateView(UpdateView):
    model = ActividadGuarderia
    form_class = ActividadGuarderiaForm
    template_name = 'app_guarderia/actividad_guarderia/form.html'
    success_url = reverse_lazy('actividad_guarderia_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Editar {self.object.nombre_actividad}'
        return context

class ActividadGuarderiaDeleteView(DeleteView):
    model = ActividadGuarderia
    template_name = 'app_guarderia/actividad_guarderia/delete.html'
    success_url = reverse_lazy('actividad_guarderia_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Eliminar {self.object.nombre_actividad}'
        return context

# CRUD Views for AsistenciaNino
class AsistenciaNinoListView(ListView):
    model = AsistenciaNino
    template_name = 'app_guarderia/asistencia_nino/list.html'
    context_object_name = 'object_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Asistencias de Niños'
        return context

class AsistenciaNinoDetailView(DetailView):
    model = AsistenciaNino
    template_name = 'app_guarderia/asistencia_nino/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Asistencia de {self.object.id_nino}'
        return context

class AsistenciaNinoCreateView(CreateView):
    model = AsistenciaNino
    form_class = AsistenciaForm
    template_name = 'app_guarderia/asistencia_nino/form.html'
    success_url = reverse_lazy('asistencia_nino_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Nueva Asistencia'
        return context

class AsistenciaNinoUpdateView(UpdateView):
    model = AsistenciaNino
    form_class = AsistenciaForm
    template_name = 'app_guarderia/asistencia_nino/form.html'
    success_url = reverse_lazy('asistencia_nino_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Editar Asistencia de {self.object.id_nino}'
        return context

class AsistenciaNinoDeleteView(DeleteView):
    model = AsistenciaNino
    template_name = 'app_guarderia/asistencia_nino/delete.html'
    success_url = reverse_lazy('asistencia_nino_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Eliminar Asistencia de {self.object.id_nino}'
        return context

# CRUD Views for PagoMensualidad
class PagoMensualidadListView(ListView):
    model = PagoMensualidad
    template_name = 'app_guarderia/pago_mensualidad/list.html'
    context_object_name = 'object_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Pagos de Mensualidades'
        return context

class PagoMensualidadDetailView(DetailView):
    model = PagoMensualidad
    template_name = 'app_guarderia/pago_mensualidad/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Pago de {self.object.id_nino}'
        return context

class PagoMensualidadCreateView(CreateView):
    model = PagoMensualidad
    form_class = PagoForm
    template_name = 'app_guarderia/pago_mensualidad/form.html'
    success_url = reverse_lazy('pago_mensualidad_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Nuevo Pago'
        return context

class PagoMensualidadUpdateView(UpdateView):
    model = PagoMensualidad
    form_class = PagoForm
    template_name = 'app_guarderia/pago_mensualidad/form.html'
    success_url = reverse_lazy('pago_mensualidad_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Editar Pago de {self.object.id_nino}'
        return context

class PagoMensualidadDeleteView(DeleteView):
    model = PagoMensualidad
    template_name = 'app_guarderia/pago_mensualidad/delete.html'
    success_url = reverse_lazy('pago_mensualidad_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Eliminar Pago de {self.object.id_nino}'
        return context
