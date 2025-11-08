import pytest
import numpy as np
import Calculadora as calc  # nome do arquivo com seu código

# ==============================================================
# TESTES DE OPERAÇÕES BÁSICAS
# ==============================================================

def test_adicao_bug():
    """A adição está somando o número duas vezes (1 + np.add(1,2)) = 4."""
    resultado = calc.adicao(1, 2)
    assert resultado == 3, f"Esperado 3, obtido {resultado}"

def test_subtracao():
    assert calc.subtracao(10, 5) == 5
    assert calc.subtracao(5, 10) == -5

def test_multiplicacao():
    assert calc.multiplicacao(3, 4) == 12
    assert calc.multiplicacao(-2, 3) == -6

def test_divisao_normal():
    assert calc.divisao(10, 2) == 5

def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        calc.divisao(10, 0)

# ==============================================================
# TESTES DE POTENCIAÇÃO E RAIZ
# ==============================================================

def test_potencia():
    assert calc.potencia(2, 3) == 8
    assert calc.potencia(9, 0.5) == 3

def test_raiz_quadrada_positiva():
    assert calc.raiz_quadrada(9) == 3

def test_raiz_quadrada_negativa():
    assert calc.raiz_quadrada(-4) == "Erro: Raiz quadrada de número negativo"

# ==============================================================
# TESTES DE FATORIAL
# ==============================================================

def test_fatorial_positivo_bug():
    """O fatorial está incorreto — o loop inclui 0 e multiplica por 0."""
    resultado = calc.fatorial(5)
    assert resultado == 120, f"Esperado 120, obtido {resultado}"

def test_fatorial_zero_bug():
    """Mesmo problema: deve retornar 1, mas o código retorna 0."""
    resultado = calc.fatorial(0)
    assert resultado == 1, f"Esperado 1, obtido {resultado}"

# ==============================================================
# TESTES DE LOGARITMOS
# ==============================================================

def test_logaritmo_natural_bug():
    """Testa o logaritmo natural correto após correção."""
    resultado = calc.logaritmo_natural(10)
    assert round(resultado, 5) == round(np.log(10), 5)


def test_logaritmo_base10_bug():
    """Está usando np.log (ln) em vez de np.log10."""
    resultado = calc.logaritmo_base10(100)
    assert round(resultado, 2) == 2.00, f"Esperado 2, obtido {resultado}"

def test_logaritmo_base10_negativo():
    """Deve retornar mensagem de erro ao usar número negativo."""
    assert calc.logaritmo_base10(-1) == "Erro: Logaritmo de número não positivo"

def test_logaritmo_base10_zero_bug():
    """Esperado erro, mas o código retorna -inf."""
    resultado = calc.logaritmo_base10(0)
    assert resultado == "Erro: Logaritmo de número não positivo"

# ==============================================================
# TESTES DE FUNÇÕES TRIGONOMÉTRICAS
# ==============================================================

@pytest.mark.parametrize("func_name, valor, esperado", [
    ("seno", np.pi/2, 1.0),
    ("cosseno", 0, 1.0),
    ("tangente", np.pi/4, 1.0),
])
def test_funcoes_trigonometricas(func_name, valor, esperado):
    """Verifica se seno, cosseno e tangente existem e funcionam corretamente."""
    if hasattr(calc, func_name):
        func = getattr(calc, func_name)
        resultado = round(func(valor), 5)
        assert resultado == pytest.approx(esperado, rel=1e-5), \
            f"{func_name}({valor}) incorreto: esperado {esperado}, obtido {resultado}"
    else:
        pytest.skip(f"Função {func_name} ainda não implementada.")

# ==============================================================
# TESTE DE MENU E INTERFACE (SMOKE TEST)
# ==============================================================

def test_menu_output(capsys):
    """Verifica se o menu imprime as opções esperadas."""
    calc.menu()
    captured = capsys.readouterr()
    assert "Calculadora Científica" in captured.out
    assert "Adição" in captured.out
    assert "Tangente" in captured.out
