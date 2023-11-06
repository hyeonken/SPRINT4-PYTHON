from datetime import datetime
import time
import json

lista = []
lista_cadastro = []
cadastro_feito = 0
login_feito = 0
dicionario = {}

def formatar_data_hora(recv_time):
    # Converte o formato de tempo do JSON para o formato desejado
    data_hora = datetime.strptime(recv_time, "%Y-%m-%dT%H:%M:%S.%fZ")
    return data_hora.strftime("%d/%m/%Y, %H:%M:%S")

def menu_aquatank1():
    if cadastro_feito == 0 or login_feito == 0:
        print('----------------------------------------------')
        print('                  \033[34mAquatank\033[m                ')
        print('----------------------------------------------\n')
        print('1 - Cadastro no site da Aquatank') #Mexer
        print('2 - Login no site da Aquatank') #Mexer (opcional)
        print('3 - Encerrar o programa\n')
        print('----------------------------------------------\n')
        try:
            escolha_menu1 = int(input("Escolha uma dessas duas opções: "))
            print()
        except ValueError:
            print("\033[31mDigite um número inteiro!\033[m\n")   
        return escolha_menu1
 
def menu_aquatank2():
    while True:
        try:
            print('----------------------------------------------')
            print('                  \033[34mAquatank\033[m                ')
            print('----------------------------------------------\n')
            print('1 - Conferir os últimos componentes da Aquatank')
            print('2 - Ver dashboard')
            print('3 - Suporte especializado')
            print('4 - Mostrar todas as operações realizadas')
            print('5 - Encerrar o programa\n')
            print('----------------------------------------------\n')

            escolha_menu2 = int(input("Escolha uma dessas duas opções: "))
            print()
        
            match escolha_menu2:
                case 1: 
                    print("Últimos componentes da Aquatank:") 
                    print("                    --                      ") 
                    print("Placa DOIT ESP32 (Bluetooth e Wifi)")
                    print("Sensor Nivel Lateral Água Arduino - Tipo Boia")
                    print("Módulo Sensor de Luz (ldr)")
                    print("Sensor de Qualidade do Ar - C02 e TVOC")
                    print("Sensor de Temperatura e Umidade - DHT11")
                    print("                    --                      \n")
                    lista.append('Olhar últimos componentes da Aquatank')
                case 2:
                    print('----------------------------------------------')
                    print('                  \033[34mAquatank\033[m                ')
                    print('----------------------------------------------\n')
                    print("Escolha o sensor que deseja visualizar:")
                    print()
                    print("1 - Temperatura")
                    print("2 - Boia")
                    print("3 - Codois")
                    print("4 - TVOC")
                    print("5 - Umidade")
                    print("6 - Luminosidade")
                    print()
                    try:
                        escolha_sensor = int(input("Escolha o sensor (1-6): "))
                        quantidade_leituras = int(input("Digite a quantidade de leituras desejada (max: 50): "))
                    except ValueError:
                        print()
                        print("Opção inválida. Por favor, insira um número válido.")
                        print()
                        continue
                    
                    if escolha_sensor < 1 or escolha_sensor > 6:
                        print()
                        print("Sensor inválido. Por favor, escolha uma opção de sensor válida.")
                        print()
                        continue
                    
                    if quantidade_leituras > 50:
                        print()
                        print("A quantidade de leituras não pode ser maior que 50.")
                        print()
                        continue
                    
                    with open('dashboard.json', 'r', encoding='utf-8') as arquivo:
                        dados = json.load(arquivo)
                        
                        for sensor_data in dados:
                            sensor_name = sensor_data['name']
                            sensor_values = sensor_data['values']
                            
                            if escolha_sensor == 1 and sensor_name != 'temperature':
                                continue
                            elif escolha_sensor == 2 and sensor_name != 'boia':
                                continue
                            elif escolha_sensor == 3 and sensor_name != 'codois':
                                continue
                            elif escolha_sensor == 4 and sensor_name != 'tvoc':
                                continue
                            elif escolha_sensor == 5 and sensor_name != 'humidity':
                                continue
                            elif escolha_sensor == 6 and sensor_name != 'luminosity':
                                continue

                            sensor_nome_dash = sensor_name
                            unidade_sensor = ""
                            
                            if sensor_name == 'temperature':
                                sensor_nome_dash = "Temperatura"
                                unidade_sensor = "°C"
                            elif sensor_name == 'boia':
                                sensor_nome_dash = "Boia"
                                unidade_sensor = ""
                            elif sensor_name == 'codois':
                                sensor_nome_dash = "Co2"
                                unidade_sensor = "ppm"
                            elif sensor_name == 'tvoc':
                                sensor_nome_dash = "Tvoc"
                                unidade_sensor = "µg/m³"
                            elif sensor_name == 'humidity':
                                sensor_nome_dash = "Umidade"
                                unidade_sensor = "%"
                            elif sensor_name == 'luminosity':
                                sensor_nome_dash = "Luminosidade"
                                unidade_sensor = "%"

                            print()
                            print(f"\033[34mÚltimas {quantidade_leituras} leituras de {sensor_nome_dash}:\033[m")
                            print()
                            
                            for value in sensor_values[-quantidade_leituras:]:
                                valores = value['attrValue']
                                data_hora = value['recvTime']
                                data_hora_formatados = datetime.strptime(data_hora, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d/%m/%Y, %H:%M:%S")
                                print(f"{valores} {unidade_sensor} - {data_hora_formatados}")
                                print()
                        lista.append('Ver dashboard')
                case 3:
                    alguma_duvida = input("Você tem alguma dúvida sobre o Aquatank? (sim/não): ").lower()
                    print()
                    if   alguma_duvida == "sim" or alguma_duvida == "s":
                        for i in range(5):
                            i = "."
                            print(i)

                        num = int(input("Digite a quantidade de dúvidas: "))
                        print()
                        contador = 0
                        while contador < num:
                            duvida = input(f"Escreva sua {contador + 1}ª dúvida ao lado: ")
                            print(f"{duvida}\n")
                            contador += 1
                            dicionario[contador] = duvida 
                            print(dicionario)
                            
                        print("\nAgradecemos pelas dúvidas. Ela será analisada e retornada em breve no seu e-mail...\n")
                        lista.append("Suporte especializado - Teve dúvida")
                     
                    else:  
                        lista.append("Suporte especializado - Não teve nenhuma dúvida")  
                case 4: 
                    print()
                    resposta = input("Deseja ver o resumo de operações realizadas do menu? (sim/não): ").lower()
                    print()
                    if resposta == "não" or resposta == "n" or resposta == "nao":
                        print("Obrigado por utilizar o programa!")   
                    elif resposta == "sim" or resposta == "s":
                        print("Resumo das operações realizadas:")
                        print()
                        for n in lista:
                            print(f"\033[34m{n}\033[m")
                    print()
                    resposta2 = input("Deseja continuar? (sim/não): ").lower()
                    print() 
                    if resposta2 == "não" or resposta2 == "n" or resposta2 == "nao":
                        print("Obrigado pela compreensão! Te esperamos em breve novamente!\n") 
                        return True
                    else:
                        lista.append("Mostrar todas as operações realizadas")        
                case 5:
                    return True
                case _:
                    print("\033[31mError!! Número inválido!\033[m \n")
        except ValueError:
            print("\033[31mDigite um número inteiro!\033[m\n")                

def validar_email(email):
    if "@" in email and "." in email:
        return True
    return False

# Função para validar a senha
def validar_senha(senha):
    if len(senha) >= 8:
        return True
    return False

nome = ""
email_valido = False
senha_valida = False

while True:
    escolha_menu1 = menu_aquatank1() 

    if escolha_menu1 == 1:
        current_time = datetime.now()
        print("Hora atual:", current_time.strftime("%H:%M:%S"))
        time.sleep(1)

        while True:
            nome = input('Digite o seu nome: ')
            email = input('Informe seu e-mail: ')
            senha = input('Digite sua senha (8 caracteres): ')
            print()

            email_valido = validar_email(email)
            senha_valida = validar_senha(senha)

            if email_valido and senha_valida:
                break
            else:
                if not email_valido and not senha_valida:
                    print("\033[31mEmail e senha inválidos! Tente novamente!\033[m\n")
                elif not email_valido:
                    print("\033[31mEmail inválido! Certifique-se de usar um formato de email válido.\033[m\n")
                elif not senha_valida:
                    print("\033[31mSenha inválida! A senha deve ter pelo menos 8 caracteres.\033[m\n")

        email_existente = False
        with open('cadastro.json', 'r', encoding='utf-8') as arquivo:
            lista_cadastro = json.load(arquivo)
            for cadastro_existente in lista_cadastro:
                if cadastro_existente['e-mail'] == email:
                    email_existente = True

            if email_existente == True:
                print("\n\033[31mEste email já está cadastrado! Tente com um email diferente.\033[m")
            else:
                cadastro = {'nome': nome, 'e-mail': email, 'senha': senha}
                lista_cadastro.append(cadastro)

        try:
            with open('cadastro.json', 'w', encoding='utf-8') as arquivo:
                json.dump(lista_cadastro, arquivo, indent=4, ensure_ascii=False)
        except IOError:
            print("\n\033[31mErro ao salvar o cadastro. Por favor, tente novamente.\033[m")

    elif escolha_menu1 == 2:
        current_time = datetime.now()
        print("Hora atual:", current_time.strftime("%H:%M:%S"))
        time.sleep(1)
        email_valido = False
        senha_valida = False
        while not (email_valido and senha_valida):
            email = input('Informe seu e-mail: ')
            senha = input('Digite sua senha(8 caracteres): ')

            email_valido = validar_email(email)
            senha_valida = validar_senha(senha)

            if not email_valido and not senha_valida:
                print("\n\033[31mEmail e senha inválidos! Tente novamente!\033[m\n")
            elif not email_valido:
                print("\n\033[31mEmail inválido! Tente novamente!\033[m\n")
            elif not senha_valida:    
                print("\n\033[31mSenha inválida! Tente novamente!\033[m\n")

        if'@' in email and len(senha)>=8:
            print("\nVerificando sua conta...")
            for i in range(5):
                i = "."
                print(i)
            print("Sincronizando com a sua conta...")
            for i in range(5):
                i = "."
                print(i)
            print("\n\033[32mSeja bem-vindo ao Aquatank!\033[m\n")
            login_feito = 1
            lista.append('Login no site da Aquatank.')
            retorno = menu_aquatank2()
            if retorno == True:
                break
            
    elif escolha_menu1 == 3:
        break
    else:
        print("\033[31mError!! Número inválido!\033[m \n")