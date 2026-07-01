from paciente import Paciente


class PacienteParticular(Paciente):
    """
    Subclasse que representa um paciente que paga diretamente pelo atendimento.
    Herda de Paciente e adiciona funcionalidades específicas para pagamentos particulares.
    """
    
    def __init__(self, nome, data_nascimento, cpf, telefone, tipo_sanguineo, 
                 numero_prontuario, forma_pagamento, desconto_fidelidade):
        """
        Inicializa um paciente particular.
        
        Args:
            nome (str): Nome completo do paciente
            data_nascimento (str): Data de nascimento no formato "DD/MM/AAAA"
            cpf (str): CPF do paciente
            telefone (str): Número de contato
            tipo_sanguineo (str): Tipo sanguíneo
            numero_prontuario (str): Identificador único na clínica
            forma_pagamento (str): Forma de pagamento (ex: "Cartão", "Pix", "Dinheiro")
            desconto_fidelidade (float): Desconto por fidelidade (ex: 0.10 = 10%)
        """
        super().__init__(nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario)
        self.forma_pagamento = forma_pagamento
        self.desconto_fidelidade = desconto_fidelidade
    
    def calcular_valor_final(self, valor_consulta, taxa_urgencia=0):
        """
        Calcula o valor final da consulta com taxa de urgência e desconto de fidelidade.
        
        Args:
            valor_consulta (float): Valor base da consulta
            taxa_urgencia (float): Taxa adicional para atendimentos urgentes (padrão: 0)
        
        Returns:
            float: Valor final após aplicar taxa e desconto
        """
        valor_com_taxa = valor_consulta + taxa_urgencia
        desconto_aplicado = valor_com_taxa * self.desconto_fidelidade
        valor_final = valor_com_taxa - desconto_aplicado
        
        print(f"\n{'='*50}")
        print(f"CÁLCULO DE VALOR - PACIENTE PARTICULAR")
        print(f"{'='*50}")
        print(f"Valor da consulta: R$ {valor_consulta:.2f}")
        print(f"Taxa de urgência: R$ {taxa_urgencia:.2f}")
        print(f"Subtotal: R$ {valor_com_taxa:.2f}")
        print(f"Desconto de fidelidade ({self.desconto_fidelidade*100:.0f}%): -R$ {desconto_aplicado:.2f}")
        print(f"VALOR FINAL: R$ {valor_final:.2f}")
        print(f"Forma de pagamento: {self.forma_pagamento}")
        
        return valor_final
    
    def exibir_informacoes(self, detalhado=False):
        """
        Exibe informações do paciente particular, incluindo dados da superclasse.
        
        Args:
            detalhado (bool): Se True, exibe informações completas
        """
        super().exibir_informacoes(detalhado)
        print(f"Forma de Pagamento: {self.forma_pagamento}")
        print(f"Desconto de Fidelidade: {self.desconto_fidelidade*100:.0f}%")
        print(f"{'='*50}\n")
