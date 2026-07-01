# Sistema de Gerenciamento de Pacientes - Clínica Médica

## 📋 Descrição do Projeto

Este projeto implementa um sistema de gerenciamento de pacientes para uma clínica médica utilizando os pilares da **Programação Orientada a Objetos (POO)** em Python. O sistema distingue entre dois tipos de pacientes:

- **Pacientes Particulares**: Que pagam diretamente pelo atendimento
- **Pacientes por Convênio**: Que são atendidos via plano de saúde

Através de herança, polimorfismo e sobrescrita, o projeto demonstra como modelar diferentes tipos de entidades que compartilham características comuns mas possuem comportamentos distintos.

---

##  Estrutura de Classes

### 1. **Paciente** (Superclasse)

Classe base que representa um paciente da clínica, contendo atributos e métodos comuns a qualquer tipo de paciente.

#### Atributos:
- `nome` (str): Nome completo do paciente
- `data_nascimento` (str): Data no formato "DD/MM/AAAA"
- `_cpf` (str): CPF do paciente (privado)
- `telefone` (str): Número de contato
- `tipo_sanguineo` (str): Ex: "A+", "O-", "AB+"
- `numero_prontuario` (str): Identificador único na clínica

#### Métodos:
- `registrar_atendimento(tipo, custo)`: Registra um atendimento do paciente
- `exibir_informacoes(detalhado)`: Exibe informações do paciente
  - Se `detalhado=False`: Mostra apenas nome, prontuário e tipo sanguíneo
  - Se `detalhado=True`: Mostra todos os atributos

---

### 2. **PacienteParticular** (Subclasse)

Herda de `Paciente` e adiciona funcionalidades específicas para pagamentos particulares.

#### Atributos Adicionais:
- `forma_pagamento` (str): Ex: "Cartão", "Pix", "Dinheiro"
- `desconto_fidelidade` (float): Desconto em decimal (ex: 0.10 = 10%)

#### Métodos:
- `calcular_valor_final(valor_consulta, taxa_urgencia)`: Calcula o valor final
  - Aplica taxa de urgência ao valor base
  - Aplica desconto de fidelidade
  - Retorna o valor final
- `exibir_informacoes(detalhado)`: Sobrescreve o método da superclasse
  - Chama `super().exibir_informacoes()` e adiciona informações específicas

---

### 3. **PacienteConvenio** (Subclasse)

Herda de `Paciente` e adiciona funcionalidades específicas para atendimentos por convênio.

#### Atributos Adicionais:
- `nome_convenio` (str): Ex: "Unimed", "Amil"
- `numero_carteirinha` (str): Número da carteirinha do convênio

#### Métodos:
- `registrar_autorizacao(procedimento, valor_glosa)`: Registra autorização do convênio
  - Exibe procedimento autorizado
  - Exibe valor da glosa (se houver)
- `exibir_informacoes(detalhado)`: Sobrescreve o método da superclasse
  - Chama `super().exibir_informacoes()` e adiciona informações específicas

---

##  Conceitos de POO Implementados

### ✓ **Herança**
- `PacienteParticular` e `PacienteConvenio` herdam de `Paciente`
- Uso de `super().__init__()` para inicializar atributos da superclasse

### ✓ **Polimorfismo**
- Método `exibir_informacoes()` é sobrescrito nas subclasses
- Cada subclasse pode chamar a superclasse através de `super()`

### ✓ **Encapsulamento**
- Atributo `_cpf` prefixado com `_` indica atributo privado
- Histórico de atendimentos e autorizações armazenados como privados

### ✓ **Sobrescrita**
- `PacienteParticular` e `PacienteConvenio` sobrescrevem `exibir_informacoes()`
- Complementam o comportamento com `super().exibir_informacoes()`

---

## 📂 Estrutura de Arquivos

```
avaliacao_02/
├── paciente.py              # Classe base Paciente
├── paciente_particular.py   # Subclasse PacienteParticular
├── paciente_convenio.py     # Subclasse PacienteConvenio
├── main.py                  # Demonstração de uso
└── README.md                # Este arquivo
```

---

##  Como Executar

### 1. Clonar ou baixar o projeto:
```bash
git clone <seu-repositorio>
cd avaliacao_02
```

### 2. Executar o programa principal:
```bash
python main.py
```

---

##  Exemplo de Execução

Ao executar `python main.py`, você verá:

```
============================================================
SISTEMA DE GERENCIAMENTO DE PACIENTES - CLÍNICA MÉDICA
============================================================


CRIANDO PACIENTE PARTICULAR...
------------------------------------------------------------
✓ Paciente particular criado com sucesso!

==================================================
INFORMAÇÕES DETALHADAS DO PACIENTE
==================================================
Nome: João Silva
Data de Nascimento: 15/03/1985
CPF: 123.456.789-00
Telefone: (11) 98765-4321
Tipo Sanguíneo: O+
Número do Prontuário: PAC001
Forma de Pagamento: Cartão de Crédito
Desconto de Fidelidade: 10%
==================================================

✓ Atendimento registrado para João Silva
  Tipo: Consulta Geral | Custo: R$ 150.00

==================================================
CÁLCULO DE VALOR - PACIENTE PARTICULAR
==================================================
Valor da consulta: R$ 200.00
Taxa de urgência: R$ 50.00
Subtotal: R$ 250.00
Desconto de fidelidade (10%): -R$ 25.00
VALOR FINAL: R$ 225.00
Forma de pagamento: Cartão de Crédito
==================================================


CRIANDO PACIENTE POR CONVÊNIO...
------------------------------------------------------------
✓ Paciente por convênio criado com sucesso!

==================================================
INFORMAÇÕES DETALHADAS DO PACIENTE
==================================================
Nome: Maria Santos
Data de Nascimento: 22/07/1990
CPF: 987.654.321-11
Telefone: (11) 99876-5432
Tipo Sanguíneo: A-
Número do Prontuário: PAC002
Convênio: Unimed
Número da Carteirinha: UNI-123456789
==================================================

✓ Atendimento registrado para Maria Santos
  Tipo: Consulta Cardiologia | Custo: R$ 300.00

==================================================
AUTORIZAÇÃO DO CONVÊNIO
==================================================
Procedimento Autorizado: Eletrocardiograma
Convênio: Unimed
Carteirinha: UNI-123456789
Valor da Glosa: R$ 25.50
==================================================

...

============================================================
RESUMO DO SISTEMA
============================================================

✓ Total de pacientes cadastrados: 4
  - 2 Pacientes Particulares
  - 2 Pacientes por Convênio

✓ Demonstrações realizadas:
  - Herança de classes
  - Polimorfismo de métodos (exibir_informacoes)
  - Métodos específicos de cada subclasse
  - Cálculo de valores com taxa e desconto
  - Registro de autorizações de convênio

============================================================
```

---

##  Aluno

**George Soares Jonard** 

---


---

