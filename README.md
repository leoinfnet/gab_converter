# 🔄 Conversor de Medidas

![Coverage](./coverage.svg)
[![Coverage Status](https://img.shields.io/badge/coverage-pending-yellow)](#)
[![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue)](#)
[![License](https://img.shields.io/badge/license-MIT-green)](#)

Projeto didático em Python para demonstrar **CI com GitHub Actions**.  
Um CLI bonitinho (Typer + Rich) que converte:

- 🌡️ Temperaturas → Celsius, Fahrenheit e Kelvin  
- 📏 Distâncias → Quilômetros ↔︎ Milhas  
- ⚖️ Peso → Quilos ↔︎ Libras  

---

## ✨ Demonstração

```bash
$ python -m conversor.cli menu
```

Exemplo de saída:

```python-repl
Conversor de Medidas • Typer + Rich

1 - Celsius → Fahrenheit
2 - Fahrenheit → Celsius
...
7 - Quilos → Libras
8 - Libras → Quilos

Digite o número: 1
Digite o valor: 25
25 °C → 77 °F
```

---

## 🚀 Instalação

Crie um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🧪 Testes

Rodar com **pytest**:

```bash
pytest -q
```

Exemplo de saída:

```
....                                                                     [100%]
4 passed in 0.05s
```

---

## ⚙️ CI com GitHub Actions

O pipeline (`.github/workflows/ci.yml`) executa:

1. Instalação das dependências  
2. Execução dos testes automatizados  
3. (Opcional) Linter/formatador (Ruff, Black, etc.)

---

## 📊 Cobertura de Testes

Você pode adicionar cobertura com `pytest-cov`:

```bash
pip install pytest-cov
pytest --cov=conversor --cov-report=term-missing
```

E integrar com [Codecov](https://about.codecov.io/) ou [Coveralls](https://coveralls.io/) para atualizar o badge automaticamente.

---

## 📦 Roadmap para Aula

- ✅ Projeto inicial com CLI + testes  
- ✅ Workflow de CI no GitHub Actions  
- 🔜 Adicionar cobertura de testes (Codecov/Coveralls)  
- 🔜 Adicionar formatador/linter (Black, Ruff)  
- 🔜 Criar release automática com PyInstaller (executável)  

---

## 📜 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais detalhes.
