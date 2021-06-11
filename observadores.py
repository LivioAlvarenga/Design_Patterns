
from typing import Any


def envia_nf_por_email(nota_fiscal: Any):
    """Envia email assim que uma NF é criada. Padrão observadores aplicado.

    Args:
        nota_fiscal.py (class Nota_fiscal): Cria Nota fiscal
    """
    print(f'\nEnviando nota fiscal {nota_fiscal.cnpj} por e-mail.')


def salva_nf_no_banco(nota_fiscal: Any):
    """Salva NF no banco de dados assim que uma NF é criada. Padrão
    observadores aplicado.

    Args:
        nota_fiscal.py (class Nota_fiscal): Cria Nota fiscal
    """
    print(f'\nSalvando nota fiscal {nota_fiscal.cnpj} no banco de dados.')


def imprime_nf(nota_fiscal: Any):
    """Imprime NF assim que uma NF é criada. Padrão observadores aplicado.

    Args:
        nota_fiscal.py (class Nota_fiscal): Cria Nota fiscal
    """
    print(f'\nImprimindo nota fiscal {nota_fiscal.cnpj}.')
