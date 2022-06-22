#Uma grande emissora de televisão quer fazer uma enquete entre os seustelespectadores para saber qual o melhor jogador
#após cada jogo. Para isto,faz-se necessário o desenvolvimento de um programa, que será utilizado pelastelefonistas, 
#para a computação dos votos. Sua equipe foi contratada paradesenvolver este programa, utilizando a linguagem de programação
#python. Para computar cada voto, o usuario digitará um número, entre 1 e 23,correspondente ao número da camisa do jogador.
#Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, oprograma deve
#ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa 
#deverá exibir:a. O total de votos computados;b. Os números e respectivos votos de todos os jogadores que receberam votos
#;c. O percentual de votos de cada um destes jogadores;d. O número do jogador escolhido como o melhor jogador da partida,
#juntamente com o número de votos e o percentual de votos dados a ele.
#
# Observe que os votos inválidos e o zero final não devem ser computadoscomo votos.
#O resultado aparece ordenado pelo número do jogador. Oprograma deve fazer uso de arrays. 
#O programa deverá executar o cálculodo percentual de cada jogador através de uma função.
#Esta funçãoreceberá dois parâmetros: o número de votos de um jogador e o total devotos.
#A função calculará o percentual e retornará o valor calculado.Abaixo segue uma tela de exemplo.
#O disposição das informações deve sero mais próxima possível ao exemplo. Os dados são fictícios e podemmudar a cada
#execução do programa. Ao final, o programa deve aindagravar os dados referentes ao resultado da votação em um arquivo
#texto no disco
#obedecendo a mesma disposição apresentada na tela.





jogador = 1
listaJog = []
while jogador != 0:
    if jogador > 0 and jogador < 24:
        jogador = int(input('Digite o número do jogador:(0=fim)'))
        if jogador > 0 and jogador < 24:
            listaJog.append(jogador)
    else:
        print('Digite número entre 1 e 23')
        jogador = 1
print('Resultado da votação!\nForam computados',len(listaJog),'votos!')
print(listaJog)
listaJog.sort()    
print(listaJog)
rep = 0
print('Jogador  Votos    %')
for k in range(0,len(listaJog)-1):
    if(listaJog[k]==listaJog[k+1]):
        rep+=1
        if (k==len(listaJog)-2):
            print('  ',listaJog[k] ,'     ',rep+1)
    else:
        print('  ',listaJog[k],'     ',rep+1)
        rep=0

