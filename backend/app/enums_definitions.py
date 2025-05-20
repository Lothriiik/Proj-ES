from enum import Enum

class RoleEnum(str, Enum):
    admin = "admin"
    operador = "operador"
    leitor = "leitor"

class MedidaEnum(str, Enum):
    metro = "m"
    metro_quadrado = "m²"
    quilo = "kg"
    grama = "g"
    litro = "L"
    unidade = "un"

class StatusEnum(str, Enum):
    planejado = "planejado"
    em_producao = "em_producao"
    finalizado = "finalizado"

