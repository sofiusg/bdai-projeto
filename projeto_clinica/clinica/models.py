from django.db import models


# ===================== Pessoa A =====================

class Especialidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Medico(models.Model):
    nome = models.CharField(max_length=120)
    num_cedula = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    foto = models.ImageField(upload_to='medicos/', blank=True, null=True)
    especialidade = models.ForeignKey(
        Especialidade, on_delete=models.PROTECT, related_name='medicos')

    class Meta:
        ordering = ['nome']
        verbose_name = 'médico'
        verbose_name_plural = 'médicos'

    def __str__(self):
        return self.nome


class Paciente(models.Model):
    SEXO_CHOICES = [('F', 'Feminino'), ('M', 'Masculino'), ('O', 'Outro')]

    nome = models.CharField(max_length=120)
    num_utente = models.CharField(max_length=20, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    morada = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


# ===================== Pessoa B =====================

class TipoExame(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    duracao_min = models.PositiveIntegerField(null=True, blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'tipo de exame'
        verbose_name_plural = 'tipos de exame'

    def __str__(self):
        return self.nome


class Equipamento(models.Model):
    nome = models.CharField(max_length=120)
    fabricante = models.CharField(max_length=100, blank=True)
    modelo = models.CharField(max_length=100, blank=True)
    num_serie = models.CharField(max_length=50, unique=True)
    data_aquisicao = models.DateField(null=True, blank=True)
    sala = models.CharField(max_length=50, blank=True)
    foto = models.ImageField(upload_to='equipamentos/', blank=True, null=True)
    tipos_exame = models.ManyToManyField(
        TipoExame, related_name='equipamentos', blank=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} ({self.sala})" if self.sala else self.nome


class Exame(models.Model):
    ESTADO_CHOICES = [
        ('agendado', 'Agendado'),
        ('realizado', 'Realizado'),
        ('cancelado', 'Cancelado'),
    ]

    data = models.DateField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='agendado')
    observacoes = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='exames/', blank=True, null=True)
    paciente = models.ForeignKey(
        Paciente, on_delete=models.PROTECT, related_name='exames')
    tipo_exame = models.ForeignKey(
        TipoExame, on_delete=models.PROTECT, related_name='exames')
    equipamento = models.ForeignKey(
        Equipamento, on_delete=models.PROTECT, related_name='exames')

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return f"{self.tipo_exame} - {self.paciente} ({self.data})"


# ===================== Pessoa A =====================

class Relatorio(models.Model):
    data = models.DateField()
    texto = models.TextField(blank=True)
    conclusao = models.CharField(max_length=500)
    medico = models.ForeignKey(
        Medico, on_delete=models.PROTECT, related_name='relatorios')
    exame = models.OneToOneField(
        Exame, on_delete=models.PROTECT, related_name='relatorio')

    class Meta:
        ordering = ['-data']
        verbose_name = 'relatório'
        verbose_name_plural = 'relatórios'

    def __str__(self):
        return f"Relatório de {self.exame}"