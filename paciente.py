class Paciente:
    """
    Classe base que representa um paciente da clínica médica.
    Contém atributos e métodos comuns a qualquer tipo de paciente.
    """
    
    def __init__(self, nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario):
        """
        Inicializa um paciente com seus dados básicos.
        
        Args:
            nome (str): Nome completo do paciente
            data_nascimento (str): Data de nascimento no formato "DD/MM/AAAA"
            cpf (str): CPF do paciente
            telefone (str): Número de contato
            tipo_sanguineo (str): Tipo sanguíneo (ex: "A+", "O-", "AB+")
            numero_prontuario (str): Identificador único na clínica
        """
        self.nome = nome
        self.data_nascimento = data_nascimento
        self._cpf = cpf  # Prefixo _ indica atributo privado
        self.telefone = telefone
        self.tipo_sanguineo = tipo_sanguineo
        self.numero_prontuario = numero_prontuario
        self._historico_atendimentos = []  # Atributo privado para armazenar histórico
    
    def registrar_atendimento(self, tipo, custo):
        """
        Registra um atendimento do paciente.
        
        Args:
            tipo (str): Tipo de atendimento (ex: "Consulta", "Exame")
            custo (float): Custo do atendimento
        """
        self._historico_atendimentos.append({"tipo": tipo, "custo": custo})
        print(f"✓ Atendimento registrado para {self.nome}")
        print(f"  Tipo: {tipo} | Custo: R$ {custo:.2f}")
    
    def exibir_informacoes(self, detalhado=False):
        """
        Exibe informações do paciente.
        
        Args:
            detalhado (bool): Se False, mostra apenas nome, prontuário e tipo sanguíneo.
                             Se True, mostra todos os atributos.
        """
        if detalhado:
            print(f"\n{'='*50}")
            print(f"INFORMAÇÕES DETALHADAS DO PACIENTE")
            print(f"{'='*50}")
            print(f"Nome: {self.nome}")
            print(f"Data de Nascimento: {self.data_nascimento}")
            print(f"CPF: {self._cpf}")
            print(f"Telefone: {self.telefone}")
            print(f"Tipo Sanguíneo: {self.tipo_sanguineo}")
            print(f"Número do Prontuário: {self.numero_prontuario}")
        else:
            print(f"\n{'='*50}")
            print(f"INFORMAÇÕES DO PACIENTE")
            print(f"{'='*50}")
            print(f"Nome: {self.nome}")
            print(f"Número do Prontuário: {self.numero_prontuario}")
            print(f"Tipo Sanguíneo: {self.tipo_sanguineo}")
