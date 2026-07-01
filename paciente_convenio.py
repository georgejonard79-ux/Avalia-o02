from paciente import Paciente


class PacienteConvenio(Paciente):
    """
    Subclasse que representa um paciente atendido via convênio médico.
    Herda de Paciente e adiciona funcionalidades específicas para convênios.
    """
    
    def __init__(self, nome, data_nascimento, cpf, telefone, tipo_sanguineo, 
                 numero_prontuario, nome_convenio, numero_carteirinha):
        """
        Inicializa um paciente por convênio.
        
        Args:
            nome (str): Nome completo do paciente
            data_nascimento (str): Data de nascimento no formato "DD/MM/AAAA"
            cpf (str): CPF do paciente
            telefone (str): Número de contato
            tipo_sanguineo (str): Tipo sanguíneo
            numero_prontuario (str): Identificador único na clínica
            nome_convenio (str): Nome do plano de saúde (ex: "Unimed", "Amil")
            numero_carteirinha (str): Número da carteirinha do convênio
        """
        super().__init__(nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario)
        self.nome_convenio = nome_convenio
        self.numero_carteirinha = numero_carteirinha
        self._autorizacoes = []  # Atributo privado para armazenar autorizações
    
    def registrar_autorizacao(self, procedimento, valor_glosa=0):
        """
        Registra uma autorização de procedimento do convênio.
        
        Args:
            procedimento (str): Tipo de procedimento autorizado
            valor_glosa (float): Valor da glosa, se houver (padrão: 0)
        """
        self._autorizacoes.append({"procedimento": procedimento, "glosa": valor_glosa})
        
        print(f"\n{'='*50}")
        print(f"AUTORIZAÇÃO DO CONVÊNIO")
        print(f"{'='*50}")
        print(f"Procedimento Autorizado: {procedimento}")
        print(f"Convênio: {self.nome_convenio}")
        print(f"Carteirinha: {self.numero_carteirinha}")
        if valor_glosa > 0:
            print(f"Valor da Glosa: R$ {valor_glosa:.2f}")
        else:
            print(f"Valor da Glosa: Sem glosa")
        print(f"{'='*50}\n")
    
    def exibir_informacoes(self, detalhado=False):
        """
        Exibe informações do paciente por convênio, incluindo dados da superclasse.
        
        Args:
            detalhado (bool): Se True, exibe informações completas
        """
        super().exibir_informacoes(detalhado)
        print(f"Convênio: {self.nome_convenio}")
        print(f"Número da Carteirinha: {self.numero_carteirinha}")
        print(f"{'='*50}\n")
