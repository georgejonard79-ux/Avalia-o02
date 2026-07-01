"""
Sistema de Gerenciamento de Pacientes - Clínica Médica
Demonstração de uso das classes Paciente, PacienteParticular e PacienteConvenio
"""

from paciente import Paciente
from paciente_particular import PacienteParticular
from paciente_convenio import PacienteConvenio


def main():
    print("\n" + "="*60)
    print("SISTEMA DE GERENCIAMENTO DE PACIENTES - CLÍNICA MÉDICA")
    print("="*60)
    
    # ============ DEMONSTRAÇÃO PACIENTE PARTICULAR ============
    print("\n\n📋 CRIANDO PACIENTE PARTICULAR...")
    print("-" * 60)
    
    paciente_particular = PacienteParticular(
        nome="João Silva",
        data_nascimento="15/03/1985",
        cpf="123.456.789-00",
        telefone="(11) 98765-4321",
        tipo_sanguineo="O+",
        numero_prontuario="PAC001",
        forma_pagamento="Cartão de Crédito",
        desconto_fidelidade=0.10  # 10% de desconto
    )
    
    print("✓ Paciente particular criado com sucesso!")
    paciente_particular.exibir_informacoes(detalhado=True)
    
    # Registrar atendimento
    paciente_particular.registrar_atendimento("Consulta Geral", 150.00)
    
    # Calcular valor com taxa de urgência
    valor_final = paciente_particular.calcular_valor_final(200.00, taxa_urgencia=50.00)
    
    # ============ DEMONSTRAÇÃO PACIENTE POR CONVÊNIO ============
    print("\n\n📋 CRIANDO PACIENTE POR CONVÊNIO...")
    print("-" * 60)
    
    paciente_convenio = PacienteConvenio(
        nome="Maria Santos",
        data_nascimento="22/07/1990",
        cpf="987.654.321-11",
        telefone="(11) 99876-5432",
        tipo_sanguineo="A-",
        numero_prontuario="PAC002",
        nome_convenio="Unimed",
        numero_carteirinha="UNI-123456789"
    )
    
    print("✓ Paciente por convênio criado com sucesso!")
    paciente_convenio.exibir_informacoes(detalhado=True)
    
    # Registrar atendimento
    paciente_convenio.registrar_atendimento("Consulta Cardiologia", 300.00)
    
    # Registrar autorização
    paciente_convenio.registrar_autorizacao("Eletrocardiograma", valor_glosa=25.50)
    
    # ============ OUTRO PACIENTE PARTICULAR ============
    print("\n\n📋 CRIANDO SEGUNDO PACIENTE PARTICULAR...")
    print("-" * 60)
    
    paciente_particular_2 = PacienteParticular(
        nome="Carlos Oliveira",
        data_nascimento="08/11/1975",
        cpf="555.666.777-88",
        telefone="(11) 97654-3210",
        tipo_sanguineo="B+",
        numero_prontuario="PAC003",
        forma_pagamento="Pix",
        desconto_fidelidade=0.15  # 15% de desconto
    )
    
    print("✓ Segundo paciente particular criado com sucesso!")
    paciente_particular_2.exibir_informacoes(detalhado=False)
    
    # Registrar atendimento e calcular valor
    paciente_particular_2.registrar_atendimento("Consulta Dermatologia", 180.00)
    valor_final_2 = paciente_particular_2.calcular_valor_final(180.00, taxa_urgencia=0)
    
    # ============ OUTRO PACIENTE POR CONVÊNIO ============
    print("\n\n📋 CRIANDO SEGUNDO PACIENTE POR CONVÊNIO...")
    print("-" * 60)
    
    paciente_convenio_2 = PacienteConvenio(
        nome="Ana Costa",
        data_nascimento="30/05/1988",
        cpf="111.222.333-44",
        telefone="(11) 98888-7777",
        tipo_sanguineo="AB+",
        numero_prontuario="PAC004",
        nome_convenio="Amil",
        numero_carteirinha="AMIL-987654321"
    )
    
    print("✓ Segundo paciente por convênio criado com sucesso!")
    paciente_convenio_2.exibir_informacoes(detalhado=False)
    
    # Registrar atendimento e autorização
    paciente_convenio_2.registrar_atendimento("Consulta Oftalmologia", 250.00)
    paciente_convenio_2.registrar_autorizacao("Exame de Refração", valor_glosa=0)
    
    # ============ RESUMO FINAL ============
    print("\n\n" + "="*60)
    print("RESUMO DO SISTEMA")
    print("="*60)
    print("\n✓ Total de pacientes cadastrados: 4")
    print("  - 2 Pacientes Particulares")
    print("  - 2 Pacientes por Convênio")
    print("\n✓ Demonstrações realizadas:")
    print("  - Herança de classes")
    print("  - Polimorfismo de métodos (exibir_informacoes)")
    print("  - Métodos específicos de cada subclasse")
    print("  - Cálculo de valores com taxa e desconto")
    print("  - Registro de autorizações de convênio")
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()
