from django.contrib import admin
from .models import (Especialidade, Medico, Paciente, Relatorio,
                     TipoExame, Equipamento, Exame)

# Pessoa A
admin.site.register(Especialidade)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Relatorio)

# Pessoa B
admin.site.register(TipoExame)
admin.site.register(Equipamento)
admin.site.register(Exame)