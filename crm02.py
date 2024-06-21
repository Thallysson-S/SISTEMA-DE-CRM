import mysql.connector

class Cliente:
    def __init__(self, nome, email, endereco, telefone):
        self.nome = nome
        self.email = email
        self.endereco = endereco
        self.telefone = telefone

class SistemaCRM:
    def __init__(self):
        # Estabelece a conexão com o banco de dados MySQL
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="he182555@",
            database="crm_db"
        )
        # Cria um cursor para executar consultas SQL
        self.cursor = self.conexao.cursor()

    def adicionar_cliente(self, cliente):
        try:
            # Query SQL para inserir um novo cliente na tabela 'clientes'
            sql = "INSERT INTO clientes (nome, email, endereco, telefone) VALUES (%s, %s, %s, %s)"
            # Valores a serem inseridos, obtidos dos atributos do objeto cliente
            val = (cliente.nome, cliente.email, cliente.endereco, cliente.telefone)
            # Executa a query SQL com os valores fornecidos
            self.cursor.execute(sql, val)
            # Comita a transação para efetivar a alteração no banco de dados
            self.conexao.commit()
            print("Cliente adicionado com sucesso!")
        except mysql.connector.Error as err:
            # Captura e imprime qualquer erro ocorrido durante a inserção do cliente
            print(f"Erro ao adicionar cliente: {err}")

    def listar_clientes(self):
        try:
            # Executa uma query SQL para selecionar todos os clientes da tabela 'clientes'
            self.cursor.execute("SELECT * FROM clientes")
            # Obtém todos os registros resultantes da query
            clientes = self.cursor.fetchall()
            if clientes:
                print("Lista de Clientes:")
                # Itera sobre os registros obtidos e imprime as informações de cada cliente
                for cliente in clientes:
                    print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Email: {cliente[2]}, Endereço: {cliente[3]}, Telefone: {cliente[4]}")
            else:
                print("Não há clientes cadastrados.")
        except mysql.connector.Error as err:
            # Captura e imprime qualquer erro ocorrido durante a listagem de clientes
            print(f"Erro ao listar clientes: {err}")

    def iniciar_atendimento(self):
        print("Olá! Como posso te ajudar?")
        while True:
            # Exibe um menu de opções para o usuário escolher ação desejada
            opcao = input("Opções: 1 - Adicionar Cliente | 2 - Listar Clientes | 3 - Sair\nEscolha uma opção: ")
            if opcao == '1':
                # Solicita informações do novo cliente para serem inseridas
                nome = input("Nome do cliente: ")
                email = input("Email do cliente: ")
                endereco = input("Endereço do cliente: ")
                telefone = input("Telefone do cliente: ")
                # Cria um objeto Cliente com as informações fornecidas
                novo_cliente = Cliente(nome, email, endereco, telefone)
                # Chama o método adicionar_cliente para inserir o novo cliente no banco de dados
                self.adicionar_cliente(novo_cliente)
            elif opcao == '2':
                # Chama o método listar_clientes para exibir todos os clientes cadastrados
                self.listar_clientes()
            elif opcao == '3':
                # Encerra o loop e finaliza a execução do programa
                break
            else:
                print("Opção inválida. Por favor, escolha uma das opções disponíveis.")

    def fechar_conexao(self):
        # Fecha o cursor utilizado para execução de queries SQL
        self.cursor.close()
        # Fecha a conexão com o banco de dados
        self.conexao.close()
        print("Conexão com o banco de dados fechada.")

# Execução do programa principal
if __name__ == "__main__":
    # Instancia o objeto SistemaCRM para iniciar o sistema
    sistema_crm = SistemaCRM()
    # Inicia o atendimento ao usuário
    sistema_crm.iniciar_atendimento()
    # Fecha a conexão com o banco de dados ao finalizar o programa
    sistema_crm.fechar_conexao()
