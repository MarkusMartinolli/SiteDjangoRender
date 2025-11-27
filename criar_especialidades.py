from core.models import Especialidade

# Lista de especialidades comuns para oficinas
especialidades = [
    'Mecânica Geral',
    'Ar Condicionado',
    'Elétrica Automotiva',
    'Suspensão e Freios',
    'Transmissão',
    'Motor e Cilindro',
    'Pintura',
    'Funilaria',
    'Pneus e Rodas',
    'Vidros',
    'Bateria',
    'Alinhamento e Balanceamento',
    'Revisão Preventiva',
    'Diagnóstico Eletrônico',
]

# Criar especialidades se não existirem
for esp_nome in especialidades:
    Especialidade.objects.get_or_create(nome=esp_nome)

print(f"✅ {len(especialidades)} especialidades criadas/verificadas com sucesso!")
