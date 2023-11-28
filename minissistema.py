import mysql.connector
from datetime import datetime

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="batata10",
        database="mydb"
    )

def consultar_funcionarios_por_software(cursor, id_software):
    cursor.execute("""
        SELECT f.ID AS ID_Funcionario, f.Nome AS Nome_Funcionario, s.id AS ID_Software, s.licenca
        FROM funcionários f
        JOIN funcionarios_softwares fs ON f.ID = fs.ID_Funcionario
        JOIN softwares s ON fs.ID_Software = s.id
        WHERE s.id = %s
    """, (id_software,))
    
    for resultado in cursor.fetchall():
        print(resultado)


def criar_funcionario(cursor, nome, cargo, departamento, salario, data_contratacao):
    cursor.execute(f"INSERT INTO `funcionários` (Nome, Cargo, Departamento, Salario, `Data_contratacao`) VALUES (%s, %s, %s, %s, %s)",
                   (nome, cargo, departamento, salario, data_contratacao))

def criar_servidor(cursor, nome, so, armazenamento_tb, data_instalacao, custo_manutencao, status_servidor):
    cursor.execute(f"INSERT INTO servidores (Nome, SO, Armazenamento_TB, Data_Instalacao, Custo_Manutencao, Status_Servidor) VALUES (%s, %s, %s, %s, %s, %s)",
                   (nome, so, armazenamento_tb, data_instalacao, custo_manutencao, status_servidor))

def criar_hardware(cursor, hardware, modelo, quantidade, preco, total_preco):
    cursor.execute(f"INSERT INTO hardware (Hardware, Modelo, Quantidade, Preco, Total_Preco) VALUES (%s, %s, %s, %s, %s)",
                   (hardware, modelo, quantidade, preco, total_preco))

def criar_periferico(cursor, periferico, modelo, quantidade, preco, preco_total):
    cursor.execute(f"INSERT INTO perifericos (Periferico, Modelo, Quantidade, Preco, Preco_Total) VALUES (%s, %s, %s, %s, %s)",
                   (periferico, modelo, quantidade, preco, preco_total))

def criar_software(cursor, licenca, quantidade, preco, preco_total):
    cursor.execute(f"INSERT INTO softwares (Licenca, Quantidade, Preco, Preco_Total) VALUES (%s, %s, %s, %s)",
                   (licenca, quantidade, preco, preco_total))

def ler_funcionarios(cursor):
    cursor.execute("SELECT * FROM `funcionários`")
    for funcionario in cursor.fetchall():
        print(funcionario)

def ler_servidores(cursor):
    cursor.execute("SELECT * FROM servidores")
    for servidor in cursor.fetchall():
        print(servidor)

def ler_hardware(cursor):
    cursor.execute("SELECT * FROM hardware")
    for equipamento in cursor.fetchall():
        print(equipamento)

def ler_perifericos(cursor):
    cursor.execute("SELECT * FROM perifericos")
    for periferico in cursor.fetchall():
        print(periferico)

def ler_softwares(cursor):
    cursor.execute("SELECT * FROM softwares")
    for software in cursor.fetchall():
        print(software)

def atualizar_funcionario(cursor, id_funcionario, nova_coluna, novo_valor):
    cursor.execute(f"UPDATE `funcionários` SET {nova_coluna} = %s WHERE ID = %s", (novo_valor, id_funcionario))

def atualizar_servidor(cursor, id_servidor, nova_coluna, novo_valor):
    cursor.execute(f"UPDATE servidores SET {nova_coluna} = %s WHERE ID = %s", (novo_valor, id_servidor))

def atualizar_hardware(cursor, id_hardware, nova_coluna, novo_valor):
    cursor.execute(f"UPDATE hardware SET {nova_coluna} = %s WHERE ID = %s", (novo_valor, id_hardware))

def atualizar_periferico(cursor, id_periferico, nova_coluna, novo_valor):
    cursor.execute(f"UPDATE perifericos SET {nova_coluna} = %s WHERE ID = %s", (novo_valor, id_periferico))

def atualizar_software(cursor, id_software, nova_coluna, novo_valor):
    cursor.execute(f"UPDATE softwares SET {nova_coluna} = %s WHERE ID = %s", (novo_valor, id_software))

def deletar_funcionario(cursor, id_funcionario):
    cursor.execute("DELETE FROM `funcionários` WHERE ID = %s", (id_funcionario,))

def deletar_servidor(cursor, id_servidor):
    cursor.execute("DELETE FROM servidores WHERE ID = %s", (id_servidor,))

def deletar_hardware(cursor, id_hardware):
    cursor.execute("DELETE FROM hardware WHERE ID = %s", (id_hardware,))

def deletar_periferico(cursor, id_periferico):
    cursor.execute("DELETE FROM perifericos WHERE ID = %s", (id_periferico,))

def deletar_software(cursor, id_software):
    cursor.execute("DELETE FROM softwares WHERE ID = %s", (id_software,))

def obter_input(tipo, mensagem):
    while True:
        try:
            if tipo == "float":
                return float(input(mensagem))
            elif tipo == "date":
                return datetime.strptime(input(mensagem + " (YYYY-MM-DD): "), "%Y-%m-%d").date()
            elif tipo == "int":
                return int(input(mensagem))
            else:
                return input(mensagem)
        except ValueError:
            print("Por favor, insira um valor válido.")

def menu_tabela():
    print("Escolha a tabela:")
    print("1. Funcionários")
    print("2. Servidores")
    print("3. Hardware")
    print("4. Periféricos")
    print("5. Softwares")

def menu_operacoes():
    print("Escolha a operação:")
    print("1. Criar Registro")
    print("2. Ler Registros")
    print("3. Atualizar Registro")
    print("4. Deletar Registro")
    print("5. Consultar Funcionários por Software") 

def main():
    conexao = conectar()
    cursor = conexao.cursor()

    while True:
        menu_tabela()
        escolha_tabela = input("Digite o número da tabela (ou 's' para sair): ")

        if escolha_tabela.lower() == 's':
            break

        try:
            escolha_tabela = int(escolha_tabela)
        except ValueError:
            print("Digite um número válido.")
            continue

        if escolha_tabela == 1:
            tabela = "funcionários"
        elif escolha_tabela == 2:
            tabela = "servidores"
        elif escolha_tabela == 3:
            tabela = "hardware"
        elif escolha_tabela == 4:
            tabela = "perifericos"
        elif escolha_tabela == 5:
            tabela = "softwares"
        else:
            print("Tabela inválida. Tente novamente.")
            continue

        while True:
            menu_operacoes()
            escolha_operacao = input("Digite o número da operação (ou 's' para trocar de tabela): ")

            if escolha_operacao.lower() == 's':
                break

            try:
                escolha_operacao = int(escolha_operacao)
            except ValueError:
                print("Digite um número válido.")
                continue

            if escolha_operacao == 1:
                # Operação de criar registro
                dados = []
                if tabela == "funcionários":
                    for coluna in ("Nome", "Cargo", "Departamento", "Salario", "Data_contratacao"):
                        if coluna == "Data_contratacao":
                            dado = obter_input("date", f"Digite {coluna}")
                        elif coluna == "Salario":
                            dado = obter_input("float", f"Digite {coluna}")
                        else:
                            dado = obter_input("str", f"Digite {coluna}")
                        dados.append(dado)
                    criar_funcionario(cursor, *dados)

                elif tabela == "servidores":
                    for coluna in ("Nome", "SO", "Armazenamento_TB", "Data_Instalacao", "Custo_Manutencao", "Status_Servidor"):
                        dado = obter_input("str", f"Digite {coluna}")
                        dados.append(dado)
                    criar_servidor(cursor, *dados)

                elif tabela == "hardware":
                    for coluna in ("Hardware", "Modelo", "Quantidade", "Preco", "Total_Preco"):
                        if coluna == "Preco" or coluna == "Total_Preco":
                            dado = obter_input("float", f"Digite {coluna}")
                        elif coluna == "Quantidade":
                            dado = obter_input("int", f"Digite {coluna}")
                        else:
                            dado = obter_input("str", f"Digite {coluna}")
                        dados.append(dado)
                    criar_hardware(cursor, *dados)

                elif tabela == "perifericos":
                    for coluna in ("Periferico", "Modelo", "Quantidade", "Preco", "Preco_Total"):
                        if coluna == "Preco" or coluna == "Preco_Total":
                            dado = obter_input("float", f"Digite {coluna}")
                        elif coluna == "Quantidade":
                            dado = obter_input("int", f"Digite {coluna}")
                        else:
                            dado = obter_input("str", f"Digite {coluna}")
                        dados.append(dado)
                    criar_periferico(cursor, *dados)

                elif tabela == "softwares":
                    for coluna in ("Licenca", "Quantidade", "Preco", "Preco_Total"):
                        if coluna == "Preco" or coluna == "Preco_Total":
                            dado = obter_input("float", f"Digite {coluna}")
                        elif coluna == "Quantidade":
                            dado = obter_input("int", f"Digite {coluna}")
                        else:
                            dado = obter_input("str", f"Digite {coluna}")
                        dados.append(dado)
                    criar_software(cursor, *dados)

                conexao.commit()

            elif escolha_operacao == 2:
                # Operação de ler registros
                if tabela == "funcionários":
                    ler_funcionarios(cursor)
                elif tabela == "servidores":
                    ler_servidores(cursor)
                elif tabela == "hardware":
                    ler_hardware(cursor)
                elif tabela == "perifericos":
                    ler_perifericos(cursor)
                elif tabela == "softwares":
                    ler_softwares(cursor)

            elif escolha_operacao == 3:
                # Operação de atualizar registro
                id_registro = input("Digite o ID do registro que deseja atualizar: ")
                nova_coluna = input("Digite o nome da coluna que deseja atualizar: ")
                novo_valor = input("Digite o novo valor: ")
                if tabela == "funcionários":
                    atualizar_funcionario(cursor, id_registro, nova_coluna, novo_valor)
                elif tabela == "servidores":
                    atualizar_servidor(cursor, id_registro, nova_coluna, novo_valor)
                elif tabela == "hardware":
                    atualizar_hardware(cursor, id_registro, nova_coluna, novo_valor)
                elif tabela == "perifericos":
                    atualizar_periferico(cursor, id_registro, nova_coluna, novo_valor)
                elif tabela == "softwares":
                    atualizar_software(cursor, id_registro, nova_coluna, novo_valor)
                conexao.commit()

            elif escolha_operacao == 4:
                # Operação de deletar registro
                id_registro = input("Digite o ID do registro que deseja deletar: ")
                if tabela == "funcionários":
                    deletar_funcionario(cursor, id_registro)
                elif tabela == "servidores":
                    deletar_servidor(cursor, id_registro)
                elif tabela == "hardware":
                    deletar_hardware(cursor, id_registro)
                elif tabela == "perifericos":
                    deletar_periferico(cursor, id_registro)
                elif tabela == "softwares":
                    deletar_software(cursor, id_registro)
                conexao.commit()
                
            elif escolha_operacao == 5:
                id_software = input("Digite o ID do software para filtrar funcionários: ")
                consultar_funcionarios_por_software(cursor, id_software)

            else:
                print("Opção inválida. Tente novamente.")

    cursor.close()
    conexao.close()

if __name__ == "__main__":
    main()
