# Calculadora Científica — Testes com Pytest

Projeto em Python com foco em **TDD (Test-Driven Development)**.  
Inclui operações matemáticas básicas e científicas, com testes automatizados via **pytest**.

---

## Requisitos

- Python 3.10+
- Dependências:
```bash
pip install numpy pytest
```
## Estrutura

Calculadora.py          # Código principal

test_calculadora.py     # Testes automatizados

bugs.md                 # Relatório de bugs

README.md               # Instruções

## Execução

Rodar a calculadora:
```bash
python Calculadora.py
```
Rodar os testes:
```bash
pytest -v
```

## TDD

Cada bug identificado foi corrigido seguindo o ciclo:

Escrever teste → Corrigir → Refatorar → Reexecutar testes.