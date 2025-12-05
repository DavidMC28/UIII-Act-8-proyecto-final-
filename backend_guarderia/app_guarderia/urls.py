from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # PadreMadre URLs
    path('padres_madres/', views.PadreMadreListView.as_view(), name='padre_madre_list'),
    path('padre_madre/<int:pk>/', views.PadreMadreDetailView.as_view(), name='padre_madre_detail'),
    path('padre_madre/nuevo/', views.PadreMadreCreateView.as_view(), name='padre_madre_create'),
    path('padre_madre/<int:pk>/editar/', views.PadreMadreUpdateView.as_view(), name='padre_madre_update'),
    path('padre_madre/<int:pk>/eliminar/', views.PadreMadreDeleteView.as_view(), name='padre_madre_delete'),

    # Nino URLs
    path('ninos/', views.NinoListView.as_view(), name='nino_list'),
    path('nino/<int:pk>/', views.NinoDetailView.as_view(), name='nino_detail'),
    path('nino/nuevo/', views.NinoCreateView.as_view(), name='nino_create'),
    path('nino/<int:pk>/editar/', views.NinoUpdateView.as_view(), name='nino_update'),
    path('nino/<int:pk>/eliminar/', views.NinoDeleteView.as_view(), name='nino_delete'),

    # PersonalGuarderia URLs
    path('personal/', views.PersonalGuarderiaListView.as_view(), name='personal_guarderia_list'),
    path('personal/<int:pk>/', views.PersonalGuarderiaDetailView.as_view(), name='personal_guarderia_detail'),
    path('personal/nuevo/', views.PersonalGuarderiaCreateView.as_view(), name='personal_guarderia_create'),
    path('personal/<int:pk>/editar/', views.PersonalGuarderiaUpdateView.as_view(), name='personal_guarderia_update'),
    path('personal/<int:pk>/eliminar/', views.PersonalGuarderiaDeleteView.as_view(), name='personal_guarderia_delete'),

    # GrupoNinos URLs
    path('grupos/', views.GrupoNinosListView.as_view(), name='grupo_ninos_list'),
    path('grupo/<int:pk>/', views.GrupoNinosDetailView.as_view(), name='grupo_ninos_detail'),
    path('grupo/nuevo/', views.GrupoNinosCreateView.as_view(), name='grupo_ninos_create'),
    path('grupo/<int:pk>/editar/', views.GrupoNinosUpdateView.as_view(), name='grupo_ninos_update'),
    path('grupo/<int:pk>/eliminar/', views.GrupoNinosDeleteView.as_view(), name='grupo_ninos_delete'),

    # ActividadGuarderia URLs
    path('actividades/', views.ActividadGuarderiaListView.as_view(), name='actividad_guarderia_list'),
    path('actividad/<int:pk>/', views.ActividadGuarderiaDetailView.as_view(), name='actividad_guarderia_detail'),
    path('actividad/nueva/', views.ActividadGuarderiaCreateView.as_view(), name='actividad_guarderia_create'),
    path('actividad/<int:pk>/editar/', views.ActividadGuarderiaUpdateView.as_view(), name='actividad_guarderia_update'),
    path('actividad/<int:pk>/eliminar/', views.ActividadGuarderiaDeleteView.as_view(), name='actividad_guarderia_delete'),

    # AsistenciaNino URLs
    path('asistencias/', views.AsistenciaNinoListView.as_view(), name='asistencia_nino_list'),
    path('asistencia/<int:pk>/', views.AsistenciaNinoDetailView.as_view(), name='asistencia_nino_detail'),
    path('asistencia/nueva/', views.AsistenciaNinoCreateView.as_view(), name='asistencia_nino_create'),
    path('asistencia/<int:pk>/editar/', views.AsistenciaNinoUpdateView.as_view(), name='asistencia_nino_update'),
    path('asistencia/<int:pk>/eliminar/', views.AsistenciaNinoDeleteView.as_view(), name='asistencia_nino_delete'),

    # PagoMensualidad URLs
    path('pagos/', views.PagoMensualidadListView.as_view(), name='pago_mensualidad_list'),
    path('pago/<int:pk>/', views.PagoMensualidadDetailView.as_view(), name='pago_mensualidad_detail'),
    path('pago/nuevo/', views.PagoMensualidadCreateView.as_view(), name='pago_mensualidad_create'),
    path('pago/<int:pk>/editar/', views.PagoMensualidadUpdateView.as_view(), name='pago_mensualidad_update'),
    path('pago/<int:pk>/eliminar/', views.PagoMensualidadDeleteView.as_view(), name='pago_mensualidad_delete'),
]
