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
            print('1 - Ver a última atualização do Arduino')
            print('2 - Ver dashboard')
            print('3 - Suporte especializado')
            print('4 - Mostrar todas as operações realizadas')
            print('5 - Encerrar o programa\n')
            print('----------------------------------------------\n')

            escolha_menu2 = int(input("Escolha uma dessas duas opções: "))
            print()
        
            match escolha_menu2:
                case 1: 
                    print("última atualização dos componentes eletrônicos da Aquatank:") 
                    print("                    --                      ") 
                    print("Placa DOIT ESP32 (Bluetooth e Wifi)")
                    print("Sensor Nivel Lateral Água Arduino - Tipo Boia")
                    print("Módulo Sensor de Luz (ldr)")
                    print("Sensor de Qualidade do Ar - C02 e TVOC")
                    print("Sensor de Temperatura e Umidade - DHT11")
                    print("                    --                      \n")
                    lista.append('Ver a última atualização do Arduino')
                case 2:
                    print("Dashboard com os últimos valores dos sensores:")
        
                    with open('dashboard.json', 'r', encoding='utf-8') as arquivo:
                        dados = json.load(arquivo)
                        
                        for sensor_data in dados:
                            sensor_name = sensor_data['name']
                            sensor_values = sensor_data['values']

                            if sensor_name == 'temperature':
                                sensor_display_nome = "temperatura"
                            elif sensor_name == 'boia':
                                sensor_display_nome = "boia"
                            elif sensor_name == 'codois':
                                sensor_display_nome = "codois"
                            elif sensor_name == 'tvoc':
                                sensor_display_nome = "TVOC"
                            elif sensor_name == 'humidity':
                                sensor_display_nome = "umidade"
                            elif sensor_name == 'luminosity':
                                sensor_display_nome = "luminosidade"
                            else:
                                sensor_display_nome = sensor_name
                                
                            print()
                            print(f"Últimas 5 leituras de {sensor_display_nome}:")
                            print()

                            for chave in sensor_values[-5:]:
                                attr_value = chave['attrValue']
                                recv_time = chave['recvTime']
                                formatted_time = datetime.strptime(recv_time, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d/%m/%Y, %H:%M:%S")
                                print(f"{attr_value} - {formatted_time}")
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
        for cadastro_existente in lista_cadastro:
            if cadastro_existente['e-mail'] == email:
                email_existente = True

        if email_existente:
            print("\n\033[31mEste email já está cadastrado! Tente com um email diferente.\033[m")
        else:
            cadastro = {'nome': nome, 'e-mail': email, 'senha': senha}
            lista.append(cadastro)

            try:
                with open('cadastro.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(lista, arquivo, indent=4, ensure_ascii=False)
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