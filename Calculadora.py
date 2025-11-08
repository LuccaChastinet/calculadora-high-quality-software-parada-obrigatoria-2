import numpy as np

# ==============================================================
# OPERAÇÕES BÁSICAS
# ==============================================================

def adicao(x, y):
    # BUG: somava x duas vezes (x + np.add(x, y))
    return np.add(x, y)

def subtracao(x, y):
    return np.subtract(x, y)

def multiplicacao(x, y):
    return np.multiply(x, y)

def divisao(x, y):
    if y == 0:
        raise ZeroDivisionError("Divisão por zero não permitida")
    return np.divide(x, y)


def potencia(x, y):
    return np.power(x, y)

# ==============================================================
# FUNÇÕES MATEMÁTICAS AVANÇADAS
# ==============================================================

def raiz_quadrada(x):
    if x < 0:
        return "Erro: Raiz quadrada de número negativo"
    return np.sqrt(x)

def fatorial(x):
    # BUG: o loop anterior incluía 0, resultando sempre em 0
    if x < 0:
        return "Erro: Fatorial de número negativo"
    fat = 1
    for i in range(1, x + 1):
        fat *= i
    return fat

def logaritmo_natural(x):
    # BUG: np.ln não existe — substituído por np.log
    if x <= 0:
        return "Erro: Logaritmo de número não positivo"
    return np.log(x)

def logaritmo_base10(x):
    # BUG: estava usando np.log (ln) e aceitava 0
    if x <= 0:
        return "Erro: Logaritmo de número não positivo"
    return np.log10(x)

# ==============================================================
# FUNÇÕES TRIGONOMÉTRICAS
# ==============================================================

def seno(x, radianos=True):
    """Retorna o seno de um ângulo. Se radianos=False, converte de graus."""
    if not radianos:
        x = np.radians(x)
    return np.sin(x)

def cosseno(x, radianos=True):
    """Retorna o cosseno de um ângulo. Se radianos=False, converte de graus."""
    if not radianos:
        x = np.radians(x)
    return np.cos(x)

def tangente(x, radianos=True):
    """Retorna a tangente de um ângulo. Se radianos=False, converte de graus."""
    if not radianos:
        x = np.radians(x)
    return np.tan(x)

# ==============================================================
# INTERFACE (MENU E EXECUÇÃO)
# ==============================================================

def menu():
    print("Bem-vindo à Calculadora Científica")
    print("Escolha a operação que deseja realizar:")
    print("0. Sair")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potenciação")
    print("6. Raiz Quadrada")
    print("7. Fatorial")
    print("8. Logaritmo Natural (ln)")
    print("9. Logaritmo Base 10")
    print("10. Seno")
    print("11. Cosseno")
    print("12. Tangente")

def calculadora_cientifica():
    menu()
    escolha = input("Digite o número da operação: ")
    if escolha == '0':
        print("Calculadora encerrada.")
        return

    elif escolha in ['1', '2', '3', '4', '5']:
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))
        if escolha == '1':
            print("Resultado:", adicao(x, y))
        elif escolha == '2':
            print("Resultado:", subtracao(x, y))
        elif escolha == '3':
            print("Resultado:", multiplicacao(x, y))
        elif escolha == '4':
            print("Resultado:", divisao(x, y))
        elif escolha == '5':
            print("Resultado:", potencia(x, y))
    
    elif escolha == '6':
        x = float(input("Digite o número: "))
        print("Resultado:", raiz_quadrada(x))
    
    elif escolha == '7':
        x = int(input("Digite o número: "))
        print("Resultado:", fatorial(x))
    
    elif escolha == '8':
        x = float(input("Digite o número: "))
        print("Resultado:", logaritmo_natural(x))
    
    elif escolha == '9':
        x = float(input("Digite o número: "))
        print("Resultado:", logaritmo_base10(x))
    
    elif escolha == '10':
        x = float(input("Digite o ângulo em graus: "))
        print("Resultado:", seno(x, radianos=False))
    
    elif escolha == '11':
        x = float(input("Digite o ângulo em graus: "))
        print("Resultado:", cosseno(x, radianos=False))
    
    elif escolha == '12':
        x = float(input("Digite o ângulo em graus: "))
        print("Resultado:", tangente(x, radianos=False))

    else:
        print("Operação inválida. Tente novamente.")
    
    continuar = input("Deseja realizar outra operação? (s/n): ")
    if continuar.lower() == 's':
        calculadora_cientifica()

# ==============================================================
# PROTEÇÃO DE EXECUÇÃO DIRETA
# ==============================================================

if __name__ == "__main__":
    calculadora_cientifica()
