
from typing import Any


def envia_nf_por_email(nota_fiscal: Any):
    print(f'\nEnviando nota fiscal {nota_fiscal.cnpj} por e-mail.')


def salva_nf_no_banco(nota_fiscal: Any):
    print(f'\nSalvando nota fiscal {nota_fiscal.cnpj} no banco de dados.')


def imprime_nf(nota_fiscal: Any):
    print(f'\nImprimindo nota fiscal {nota_fiscal.cnpj}.')
