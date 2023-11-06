import datetime
import time
import json
import os


lista = []
cadastro_feito = 0
login_feito = 0
dicionario = {}

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
            #Adicionar a API.json para mandar os dados dos sensores.
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
                    print("última atualização dos componentes e do arduino da Aquatank:") 
                    print("                    --                      ") 
                    print("Placa DOIT ESP32 (Bluetooth e Wifi)")
                    print("Sensor Nivel Lateral Água Arduino - Tipo Boia")
                    print("Módulo Sensor de Luz (ldr)")
                    print("Sensor de Qualidade do Ar - C02 e TVOC")
                    print("Sensor de Temperatura e Umidade - DHT11")
                    print("                    --                      \n")
                    lista.append('Ver a última atualização do Arduino')
                case 2:
                    print("Dashboard com todos os dados da operação:")
                    print("Nível de água, temperatura, CO2, luminosidade, nível de luz.")
                    with open('dashboard.json', 'r', encoding='utf-8') as arquivo:
                        dados = json.load(arquivo)
                        for linhas in dados:
                            print(linhas)
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
    # Aqui você pode adicionar sua lógica de validação de email
    # Por exemplo, verificar se o email possui um "@" e um "."
    return "@" in email 

# Função para verificar a validade da senha
def validar_senha(senha):
    # Aqui você pode adicionar sua lógica de validação de senha
    # Por exemplo, verificar se a senha tem pelo menos 8 caracteres
    return len(senha) >= 8

while True:
    escolha_menu1 = menu_aquatank1() 

    if escolha_menu1 == 1:
        current_time = datetime.datetime.now()
        print("Hora atual:", current_time.strftime("%H:%M:%S"))
        time.sleep(1)

        email_valido = False
        senha_valida = False  
        
        if os.path.exists('cadastro.json'):                                 
            with open('cadastro.json', 'r', encoding='utf-8') as arquivo:   
                lista = json.load(arquivo) 

        else:
            lista = []                
            nome = input('Digite o seu nome: ')
            email = input('Informe seu e-mail: ')
            senha = input('Digite sua senha(8 caracteres): ')
            cadastro = {'nome': nome, 'e-mail': email, 'senha': senha}                  
            lista.append(cadastro)                                                   
        
            with open('cadastro.json', 'w', encoding='utf-8') as arquivo:           
                json.dump(lista, arquivo, indent=4, ensure_ascii=False)
            

                email_valido = validar_email(email)
                senha_valida = validar_senha(senha)

                if not email_valido and not senha_valida:
                    print("\n\033[31mEmail e senha inválidos! Tente novamente!\033[m\n")
                elif not email_valido:
                    print("\n\033[31mEmail inválido! Tente novamente!\033[m\n")
                elif not senha_valida:    
                    print("\n\033[31mSenha inválida! Tente novamente!\033[m\n")
     
            #     print(f'\nOlá! Poderia confirmar se está certo seu e-mail: {email}\n')
                
            # confirmacao = input('Digite (sim/não): ')
            # if confirmacao == "s" or confirmacao == "sim" or confirmacao == "Sim" or confirmacao == "S":

            #     if '@' in email and len(senha)>=8:
            #         print("\n\033[32mCadastro realizado com sucesso!\033[m\n")
            #         print(f"Seja bem vindo {nome}!\n")
            #         cadastro_feito = 1
            #         lista.append('Cadastro no site da Aquatank')
            #         retorno = menu_aquatank2()
            #         if retorno == True:
            #             break     
            # else:
            #     print()
            #     print("\033[31mTente outra vez mais tarde!\033[m\n")  

    elif escolha_menu1 == 2:
        current_time = datetime.datetime.now()
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

        #Chamar para ele voltar para cá.
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