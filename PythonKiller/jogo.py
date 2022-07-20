
#Com base no exercício da Labenu esse código tem
#o objetivo é encontrar o assassino do python
#Vamos chamar o jogo de "KillerPyhton". O universo onde se passa 
#o crime é o Python Universe (tipo Marvel Universe)
#estou escrevendo o programana usando o Qpython
#em um motog60. 


print('##################################################')
print('Houve uma assassinato no Python Universe e a situação é extremamente grave. A morte do Jhonny P. J. pode colapasar a estrutura de todas as linguagens de programação uma vez que o assassino roubou um dispositivo capaz de destruir o Language Multiverse. O seu objetivo é prender o assassino e recuperar o dispositivo. Seja cautelos@. Precisamos saber agora se você aceita resolver o caso, a sua vida pode estar em risco e a gente não se responsabiliza por novas morte.')
print('##################################################')
solic = str(input('Você aceita assumir o caso?S/N '))
print('#######################################################')
if solic == 'N':
         print('Entendemos o seu temor. Indique alguém para resolver esse problema? ')  
         namein = str(input('Digite o nome da pessoa indicada: '))
         indi=str(input('Digite o WhatsApp da pessoa indicada '))
         print('Nome do indicado: ' +namein)
         print('Número do indicado: '+indi)
         print('Agradecemos e manteremos o sigilo. Voce pode ter ajudado a salvar o mundo') 
if solic == 'S':
          print('Obrigado por aceitar o caso. Vamos deixar você a par de tudo sobre a nossa investigação. O assassino usa charadas para nos despistar, mas já descobrimos que algums de suas charadas revelam verdades sobre o caso. Já conseguimos algumas características através das testumhas e já temos alguns depoimentos. Por onde você quer começar. Você pode começar por caracteristicas ou testemunhas.')
#print('########################################################')
          begin = str(input('Por onde você quer começar?'))
          if begin == 'caracteristicas':
                    print ('Fizemos uma analise detalhada do depoimento das testemunhas e chegamos as seguintes conclusōes: @ assassin@ tem em torno de 1,77 m, usava  tênis azul e um amarelo, é canhoto e está com a perna machucada. Resumimos o que a gente achou importante. mas seria interessante você fazer a leitura dos depoimentos. provavelmente seus olhos são mais apurados e deve encontrar algo que nossa equipe deixou passar.')
                    dpoi = str(input('Você gostaria de ler os depoimentos agora? (S/N) '))
                    if dpoi == 'S':
                            print('Desculpe, mas antes de liberar o acesso, precisamos ter certeza que você não é o assassino. faremos um pequeno teste e você precisa ser aprovado')
                            
