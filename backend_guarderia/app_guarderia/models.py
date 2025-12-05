from django.db import models

class PadreMadre(models.Model):
    id_padre_madre = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono_principal = models.CharField(max_length=20)
    telefono_alternativo = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255)
    dni = models.CharField(max_length=20)
    relacion_con_nino = models.CharField(max_length=50)
    profesion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'padre_madre'
        verbose_name_plural = "Padres/Madres"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class PersonalGuarderia(models.Model):
    TURNOS = [
        ('MAÑANA', 'Mañana'),
        ('TARDE', 'Tarde'),
        ('NOCHE', 'Noche'),
        ('COMPLETO', 'Completo'),
    ]

    id_personal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    dni = models.CharField(max_length=20)
    certificaciones = models.TextField(blank=True, null=True)
    turno = models.CharField(max_length=50, choices=TURNOS)

    class Meta:
        db_table = 'personal_guarderia'
        verbose_name_plural = "Personal de Guardería"

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cargo}"

class GrupoNinos(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    nombre_grupo = models.CharField(max_length=50, unique=True)
    edad_minima = models.IntegerField()
    edad_maxima = models.IntegerField()
    id_personal_cargo = models.ForeignKey(PersonalGuarderia, on_delete=models.SET_NULL, null=True)
    num_ninos_actual = models.IntegerField(default=0)
    capacidad_maxima = models.IntegerField()
    descripcion_actividades = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'grupo_ninos'
        verbose_name_plural = "Grupos de Niños"

    def __str__(self):
        return self.nombre_grupo

class Nino(models.Model):
    GENEROS = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    id_nino = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1, choices=GENEROS)
    id_padre_madre_principal = models.ForeignKey(PadreMadre, on_delete=models.CASCADE)
    alergias = models.TextField(blank=True, null=True)
    necesidades_especiales = models.TextField(blank=True, null=True)
    grupo_asignado = models.ForeignKey(GrupoNinos, on_delete=models.SET_NULL, null=True, to_field='nombre_grupo')
    fecha_inscripcion = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'nino'
        verbose_name_plural = "Niños"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class ActividadGuarderia(models.Model):
    id_actividad = models.AutoField(primary_key=True)
    nombre_actividad = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    horario = models.CharField(max_length=100)
    duracion_minutos = models.IntegerField()
    id_grupo = models.ForeignKey(GrupoNinos, on_delete=models.CASCADE)
    material_requerido = models.TextField(blank=True, null=True)
    es_obligatoria = models.BooleanField(default=True)

    class Meta:
        db_table = 'actividad_guarderia'
        verbose_name_plural = "Actividades de Guardería"

    def __str__(self):
        return self.nombre_actividad

class AsistenciaNino(models.Model):
    id_asistencia = models.AutoField(primary_key=True)
    id_nino = models.ForeignKey(Nino, on_delete=models.CASCADE)
    fecha_asistencia = models.DateField()
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField(blank=True, null=True)
    estuvo_enfermo = models.BooleanField(default=False)
    notas_dia = models.TextField(blank=True, null=True)
    id_personal_registro = models.ForeignKey(PersonalGuarderia, on_delete=models.CASCADE)

    class Meta:
        db_table = 'asistencia_nino'
        verbose_name_plural = "Asistencias de Niños"

    def __str__(self):
        return f"Asistencia {self.id_nino} - {self.fecha_asistencia}"

class PagoMensualidad(models.Model):
    METODOS_PAGO = [
        ('EFECTIVO', 'Efectivo'),
        ('TARJETA', 'Tarjeta'),
        ('TRANSFERENCIA', 'Transferencia'),
    ]
    
    ESTADOS_PAGO = [
        ('PENDIENTE', 'Pendiente'),
        ('PAGADO', 'Pagado'),
        ('VENCIDO', 'Vencido'),
        ('CANCELADO', 'Cancelado'),
    ]

    id_pago = models.AutoField(primary_key=True)
    id_nino = models.ForeignKey(Nino, on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    concepto = models.CharField(max_length=100)
    metodo_pago = models.CharField(max_length=50, choices=METODOS_PAGO)
    mes_correspondiente = models.DateField()
    estado_pago = models.CharField(max_length=50, choices=ESTADOS_PAGO, default='PENDIENTE')
    fecha_vencimiento = models.DateField()

    class Meta:
        db_table = 'pago_mensualidad'
        verbose_name_plural = "Pagos de Mensualidad"

    def __str__(self):
        return f"Pago {self.id_nino} - {self.mes_correspondiente}"

# Create your models here.
