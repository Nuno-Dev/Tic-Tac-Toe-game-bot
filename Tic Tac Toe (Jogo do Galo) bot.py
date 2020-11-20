#----------------------------------------------------------------------------------------------#
#------------------------------------| 99292 Nuno Martins |------------------------------------#
#----------------------------------------------------------------------------------------------#

#eh_tabuleiro: universal -> booleano

def eh_tabuleiro(tab):
    """
    eh_tabuleiro recebe um argumento de qualquer tipo e devolve True
    se o argumento corresponder a um tabuleiro (ou seja, um tuplo com 3 tuplos
    em que cada um deles contem um inteiro igual a -1, 1 ou 0), caso contrario
    devolve False.
    """
    if not type(tab)==tuple:
        return False
    if len(tab)==3:
        for linha in tab:
            if not type(linha)==tuple:
                return False
            if len(linha)==3:
                for num in linha:
                    if not (num in [-1,0,1] and type(num)==int):
                        return False
            else:
                return False
    else:
        return False
    return True

#-----------------------------------------------------------------------------------------------#

#eh_posicao: universal -> booleano

def eh_posicao(pos):
    """
    eh_posicao recebe um argumento de qualquer tipo e devolve True
    se o argumento corresponder a uma posicao do tabuleiro, isto e, se for
    um inteiro entre 1 e 9 (inclusive), caso contrario devolve False.
    """    
    if type(pos)==int:
        if pos<10 and pos>0:
            return True
    return False

#-----------------------------------------------------------------------------------------------#

#obter_coluna: tabuleiro X inteiro -> vetor 

def obter_coluna(tab, n):
    """
    obter_coluna recebe dois argumentos, um tabuleiro e um inteiro com valor de 1 a 3
    (correspondente ao numero da coluna) e devolve um vetor (tuplo) com os valores
    dessa coluna. Se algum dos argumentos for invalido gera ValueError.
    """     
    if not eh_tabuleiro(tab) or not (n in [1,2,3] and type(n)==int):
        raise ValueError('obter_coluna: algum dos argumentos e invalido')
    else:
        res = ()
        for linha in tab:
            res+=(linha[n-1],)
        return res

#-----------------------------------------------------------------------------------------------#

#obter_linha: tabuleiro X inteiro -> vetor 

def obter_linha(tab, n):
    """
    obter_linha recebe dois argumentos, um tabuleiro e um inteiro com valor de 1 a 3
    (correspondente ao numero da linha) e devolve um vetor (tuplo) com os valores
    dessa linha. Se algum dos argumentos for invalido gera ValueError.
    """      
    if not eh_tabuleiro(tab) or not (n in [1,2,3] and type(n)==int):
        raise ValueError('obter_linha: algum dos argumentos e invalido')
    else:
        return tab[n-1]

#-----------------------------------------------------------------------------------------------#

#obter_diagonal: tabuleiro X inteiro -> vetor 

def obter_diagonal(tab, n):
    """
    obter_diagonal recebe dois argumentos, um tabuleiro e um inteiro com valor de 1 a 2
    (correspondente ao numero da diagonal) e devolve um vetor (tuplo) com os valores
    dessa diagonal. Se algum dos argumentos for invalido gera ValueError.
    """     
    if not eh_tabuleiro(tab) or not (n in [1,2] and type(n)==int):
        raise ValueError('obter_diagonal: algum dos argumentos e invalido')
    else:
        if n==1:
            return (tab[0][0],tab[1][1],tab[2][2])
        else:
            return (tab[2][0],tab[1][1],tab[0][2])

#-----------------------------------------------------------------------------------------------#

#tabuleiro_str: tabuleiro -> cadeia de carateres

def tabuleiro_str(tab):
    """
    tabuleiro_str recebe um tabuleiro e devolve a cadeia de caracteres que o representa,
    permitindo ao utilizador observar o tabuleiro e as jogadas que decorrem durante o jogo.
    Se o tabuleiro for invalido, a funcao gera ValueError.
    """         
    if not eh_tabuleiro(tab):
        raise ValueError('tabuleiro_str: o argumento e invalido')
    else:
        res = ''
        for j in range(3):
            for i in range(3):
                if tab[j][i]==1:
                    res+=' X '
                elif tab[j][i]==-1:
                    res+=' O '
                else:
                    res+='   '
                if i < 2:
                    res+='|'
            if j<2:
                res+='\n-----------\n'
        return res

#-----------------------------------------------------------------------------------------------#

#eh_posicao_livre: tabuleiro X posicao -> booleano

def eh_posicao_livre(tab, pos):
    """
    eh_posicao_livre recebe dois argumentos, um tabuleiro e uma posicao. A funcao devolve
    True se a posicao corresponder a uma posicao livre do tabuleiro, caso contrario retorna
    False. No caso de algum dos argumentos ser invalido, a funcao gera ValueError.
    """     
    if not eh_tabuleiro(tab) or not eh_posicao(pos):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')    
    else:
        if pos < 4:
            return tab[0][pos-1] == 0
        elif pos < 7:
            return tab[1][pos-4] == 0
        else:
            return tab[2][pos-7] == 0

#-----------------------------------------------------------------------------------------------#

#obter_posicoes_livres: tabuleiro -> vetor 

def obter_posicoes_livres(tab):
    """
    obter_posicoes_livres recebe um tabuleiro e devolve um vetor ordenado (tuplo)
    com todas as posicoes livres do tabuleiro. Caso o tabuleiro seja invalido,
    a funcao gera ValueError.
    """
    if not eh_tabuleiro(tab):
        raise ValueError('obter_posicoes_livres: o argumento e invalido')    
    else:    
        return tuple([i for i in range(1,10) if eh_posicao_livre(tab,i)])

#-----------------------------------------------------------------------------------------------#

#jogador_ganhador: tabuleiro -> inteiro

def jogador_ganhador(tab):
    """
    jogador_ganhador recebe um tabuleiro e devolve um valor inteiro a indicar 
    o jogador que ganhou o jogo no tabuleiro passado como argumento. Retorna 1
    se o jogador 'X' ganhou, retorna -1 se o vencedor foi o jogador 'O' e retorna
    0 se nenhum dos jogadores ganhou. Caso o tabuleiro seja invalido, a funcao
    gera ValueError.
    """
    if not eh_tabuleiro(tab):
        raise ValueError('jogador_ganhador: o argumento e invalido')   
    else: 
        for i in range(1,4):
            coluna = obter_coluna(tab, i)
            if sum(coluna)==3:
                return 1
            elif sum(coluna)==-3:
                return -1
            linha = obter_linha(tab, i)
            if sum(linha)==3:
                return 1
            elif sum(linha)==-3:
                return -1   
            if i<3:
                diagonal = obter_diagonal(tab, i)
                if sum(diagonal)==3:
                    return 1
                elif sum(diagonal)==-3:
                    return -1        
        return 0

#-----------------------------------------------------------------------------------------------#

#marcar_posicao: tabuleiro X inteiro X posicao -> tabuleiro

def marcar_posicao(tab, jog, pos):
    """
    marcar_posicao recebe 3 argumentos, um tabuleiro, um inteiro correspondente ao jogador 
    1 para o jogador 'X' e -1 para o jogador 'O') e uma posicao livre e devolve um novo
    tabuleiro modificado com a nova marca do jogador nessa posicao. Se algum dos 3 argumentos 
    for invalido, a funcao gera ValueError.
    """
    if not eh_tabuleiro(tab) or pos not in obter_posicoes_livres(tab) or not jog in [-1,1] or not type(jog)==int:
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')    
    else:
        tab1 = list(map(list, tab))
        if pos < 4:
            tab1[0][pos-1] = jog
        elif pos < 7:
            tab1[1][pos-4] = jog
        else:
            tab1[2][pos-7] = jog
        return tuple(map(tuple, tab1))

#-----------------------------------------------------------------------------------------------#

#escolher_posicao_manual: tabuleiro -> posicao

def escolher_posicao_manual(tab):
    """
    escolher_posicao_manual realiza a leitura de uma posicao introduzida manualmente por um jogador
    e devolve esta posicao escolhida. No caso da posicao introduzida nao corresponder a uma posicao
    livre ou o tabuleiro dado como argumento ser invalido, a funcao gera ValueError.
    """
    if not eh_tabuleiro(tab):
        raise ValueError('escolher_posicao_manual: o argumento e invalido')    
    else:
        pos = int(input('Turno do jogador. Escolha uma posicao livre: '))
        if pos not in obter_posicoes_livres(tab):
            raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')
        else:
            return pos          
        
#-----------------------------------------------------------------------------------------------#

#escolher_posicao_auto: tabuleiro X inteiro X cadeira de caracteres -> posicao

def escolher_posicao_auto(tab, jog, str1):
    """
    escolher_posicao_auto recebe um tabuleiro, um inteiro correspondente ao jogador 
    (1 para o jogador 'X' e -1 para o jogador 'O') e uma cadeia de caracteres correspondente 
    a estrategia e devolve a posicao escolhida automaticamente de acordo com a estrategia 
    selecionada. No caso de algum dos argumentos ser invalido, a funcao gera ValueError.
    """
    if not eh_tabuleiro(tab) or not (jog in [-1,1] and type(jog)==int) or not (str1 in ['basico','normal','perfeito'] and type(str1)==str):
        raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')    
    else:
        
        #vitoria_1: tabuleiro X inteiro -> posicao
        
        def vitoria_1(tab,jog):
            """
            vitoria_1 recebe um tabuleiro e um inteiro correspondente ao jogador 
            (1 para o jogador 'X' e -1 para o jogador 'O') e se o jogador tiver duas
            das suas pecas em linha e uma posicao livre entao retorna essa posicao livre.
            """
            for i in range(1,4):
                win = [(0,jog,jog), (jog,0,jog), (jog,jog,0)]
                coluna = obter_coluna(tab, i)
                linha = obter_linha(tab, i)   
                if coluna in win:
                    return i+3*win.index(coluna)
                elif linha in win:
                    return 3*i-2+win.index(linha)               
                if i!=3:
                    diagonal = obter_diagonal(tab, i)
                    if diagonal in win:
                        if i==1:
                            return i+4*win.index(diagonal)

                        else:
                            return 7-2*win.index(diagonal)
        
        #bloqueio_2: tabuleiro X inteiro -> posicao  
        
        def bloqueio_2(tab,jog):
            """
            bloqueio_2 recebe um tabuleiro e um inteiro correspondente ao jogador 
            (1 para o jogador 'X' e -1 para o jogador 'O') e se o adversario tiver duas
            das suas pecas em linha e uma posicao livre entao retorna essa posicao livre.
            """
            jog*=-1
            return vitoria_1(tab,jog)         
        
        #bifurcacao_3: tabuleiro X inteiro -> lista de posicoes
        
        def bifurcacao_3(tab, jog):
            """
            bifurcacao_3 recebe um tabuleiro e um inteiro correspondente ao jogador 
            (1 para o jogador 'X' e -1 para o jogador 'O') e se o jogador tiver duas
            linhas/colunas/diagonais que se intersectam, onde cada uma contem uma das
            suas pecas entao retorna uma lista com todas as posicoes de intersecao 
            (criando duas formas de vencer na jogada seguinte).
            """
            pos = []
            for i in range(1,4):
                for j in range(1,4):
                    if obter_coluna(tab,i).count(jog)==1 and obter_linha(tab,j).count(jog)==1 and eh_posicao_livre(tab, i+3*j-3):
                        pos+=[i+3*j-3]
                    for k in range(1,3):
                        if k==1:
                            if obter_coluna(tab,i).count(jog)==1 and obter_diagonal(tab,1).count(jog)==1 and eh_posicao_livre(tab, 1+4*(i-1)):
                                pos+=[1+4*(i-1)]
                            if obter_linha(tab,j).count(jog)==1 and obter_diagonal(tab,1).count(jog)==1 and eh_posicao_livre(tab, 1+4*(i-1)):
                                pos+=[1+4*(i-1)]
                            if obter_diagonal(tab,1).count(jog)==1 and obter_diagonal(tab,2).count(jog)==1 and eh_posicao_livre(tab, 5):
                                pos+=[5]
                        if k==2:
                            if obter_coluna(tab,i).count(jog)==1 and obter_diagonal(tab,1).count(jog)==1 and eh_posicao_livre(tab, 7-2*(i-1)):
                                pos+=[7-2*(i-1)]
                            if obter_linha(tab,j).count(jog)==1 and obter_diagonal(tab,1).count(jog)==1 and eh_posicao_livre(tab, 3+2*(i-1)):
                                pos+=[3+2*(i-1)]  
            return pos
        
        #bloqueio_de_bifurcacao_4: tabuleiro X inteiro -> posicao
        
        def bloqueio_de_bifurcacao_4(tab,jog): 
            """
            bloqueio_de_bifurcacao_4 recebe um tabuleiro e um inteiro correspondente ao jogador 
            (1 para o jogador 'X' e -1 para o jogador 'O') e se o adversario tiver apenas uma bifurcacao
            entao retorna a posicao de bloqueio dessa bifurcacao, caso contrario, retorna a posicao
            em que se cria um dois em linha para forcar o oponente a defender, desde que a defesa nao
            resulte na criacao de uma bifurcacao para o oponente.
            """            
            if len(bifurcacao_3(tab,-1*jog)) == 1 :
                return bifurcacao_3(tab,-1*jog)[0]
            else:
                for i in range(1,4):
                    if obter_coluna(tab,i).count(jog)==1:
                        col = obter_coluna(tab,i)
                        for j in range(3):
                            if col[j]==0:
                                pos1=3*j+i
                                newtab = marcar_posicao(tab, jog, pos1)
                                if len(bifurcacao_3(newtab,-1*jog)) == 0:
                                    return pos1
                                
                    if obter_linha(tab,i).count(jog)==1:
                        linha = obter_linha(tab,i)
                        for j in range(3):
                            if linha[j]==0:
                                pos1=j+1+3*(i-1)
                                newtab = marcar_posicao(tab, jog, pos1)
                                if len(bifurcacao_3(newtab,-1*jog)) == 0:
                                    return pos1
                                
                    if i < 3 and obter_diagonal(tab,i).count(jog)==1:
                        diagonal = obter_diagonal(tab,i)
                        for j in range(3):
                            if i==1:
                                if diagonal[j]==0:
                                    pos1=4*j+i
                                    newtab = marcar_posicao(tab, jog, pos1)
                                    if len(bifurcacao_3(newtab,-1*jog)) == 0:
                                        return pos1
                            else:
                                if diagonal[j]==0:
                                    pos1=7-2*j
                                    newtab = marcar_posicao(tab, jog, pos1)
                                    if len(bifurcacao_3(newtab,-1*jog)) == 0:
                                        return pos1    
        
        #centro_5: tabuleiro X inteiro -> posicao
                    
        def centro_5(tab, jog):
            """
            centro_5 recebe um tabuleiro e um inteiro correspondente ao jogador 
            (1 para o jogador 'X' e -1 para o jogador 'O') e devolve a posicao
            central (5) no caso da mesma estar livre.
            """
            if eh_posicao_livre(tab, 5):
                return 5
        
        #canto_oposto_6: tabuleiro X inteiro -> posicao
        
        def canto_oposto_6(tab, jog):
            """
            canto_oposto_6 recebe um tabuleiro e um inteiro correspondente ao jogador 
            (1 para o jogador 'X' e -1 para o jogador 'O') e se o adversario estiver num
            canto e se o canto diagonalmente oposto for uma posicao livre entao
            retorna a posicao desse canto oposto.
            """
            jog*=-1
            if obter_linha(tab,1)[0]==jog and eh_posicao_livre(tab,9):
                return 9
            if obter_linha(tab,1)[2]==jog and eh_posicao_livre(tab,7):
                return 7
            if obter_linha(tab,3)[0]==jog and eh_posicao_livre(tab,3):
                return 3
            if obter_linha(tab,3)[2]==jog and eh_posicao_livre(tab,1):
                return 1    
        
        #canto_vazio_7: tabuleiro X inteiro -> posicao
        
        def canto_vazio_7(tab, jog):
            """
            canto_vazio_7 recebe um tabuleiro e um inteiro correspondente ao jogador 
            (1 para o jogador 'X' e -1 para o jogador 'O') e se um canto for uma posicao
            livre entao devolve a posicao correspondente a esse canto.
            """
            for x in [1,3,7,9]:
                if eh_posicao_livre(tab,x):
                    return x     
        
        #lateral_vazio_8: tabuleiro X inteiro -> posicao
        
        def lateral_vazio_8(tab, jog):
            """
            lateral_vazio_8 recebe um tabuleiro e um inteiro correspondente ao jogador 
            (1 para o jogador 'X' e -1 para o jogador 'O') e se uma posicao lateral
            (que nem e o centro, nem um canto) for livre, entao retorna a posicao
            correspondente a essa posicao lateral.
            """
            for x in [2,4,6,8]:
                if eh_posicao_livre(tab,x):
                    return x  
        
        if str1=='basico':
            for i in range(2):
                if i==0: res = centro_5(tab, jog)
                if i==1: res = canto_vazio_7(tab, jog)
                if res!=None:
                    return res
            return lateral_vazio_8(tab, jog)                               
               
                
        elif str1=='normal':
            for i in range(5):
                if i==0: res = vitoria_1(tab,jog)
                if i==1: res = bloqueio_2(tab,jog)
                if i==2: res = centro_5(tab, jog)
                if i==3: res = canto_oposto_6(tab, jog)
                if i==4: res = canto_vazio_7(tab, jog)
                if res!=None:
                    return res
            return lateral_vazio_8(tab, jog)
                
                
        elif str1=='perfeito':
            for i in range(7):
                if i==0: res = vitoria_1(tab,jog)
                if i==1: res = bloqueio_2(tab,jog)
                if i==2: 
                    res = bifurcacao_3(tab, jog)
                    if res!=[]:
                        res = bifurcacao_3(tab, jog)[0]
                    else:
                        res=None
                if i==3: 
                    res = bloqueio_de_bifurcacao_4(tab,jog)
                    if res!=[]:
                        res = bloqueio_de_bifurcacao_4(tab,jog)
                    else:
                        res=None                    
                if i==4: res = centro_5(tab, jog)
                if i==5: res = canto_oposto_6(tab, jog)
                if i==6: res = canto_vazio_7(tab, jog)
                if res!=None:
                    return res
            return lateral_vazio_8(tab, jog)            
                
#-----------------------------------------------------------------------------------------------#

#jogo_do_galo: cadeia de caracteres X cadeira de caracteres -> cadeia de caracteres

def jogo_do_galo(str1, str2):
    """
    jogo_do_galo corresponde a funcao principal que permite jogar um jogo completo de Jogo do Galo 
    de um jogador contra o computador. O jogo comeca sempre com o jogador 'X' a marcar uma posicao livre
    e termina quando um dos jogadores vence ou, se nao existem posicoes livres no tabuleiro. A funcao
    recebe 2 argumentos, o primeiro e uma cadeia de caracteres a indicar o jogador ('X' ou 'O') e o segundo
    argumento e uma cadeia de caracteres a indicar a estrategia usada ('basico', 'normal' ou 'perfeito') e 
    devolve uma cadeia de caracteres a indicar o vencedor ('X' ou 'O') ou 'EMPATE' no caso de nao haver 
    vencedor. No caso de algum dos argumentos ser invalido, a funcao gera ValueError.
    """
    if not (str1 in ['X','O'] and type(str1)==str) or not (str2 in ['basico','normal','perfeito'] and type(str2)==str):
        raise ValueError('jogo_do_galo: algum dos argumentos e invalido')
    else:
        print("Bem-vindo ao JOGO DO GALO.\nO jogador joga com '{}'.".format(str1))
        tab = ((0,0,0),(0,0,0),(0,0,0))
        if str1=='X':
            jog = 1
            pos = escolher_posicao_manual(tab)
            tab = marcar_posicao(tab,jog,pos)
            print(tabuleiro_str(tab))
        else:
            jog = -1
        while len(obter_posicoes_livres(tab))!=0:
            print('Turno do computador ({}):'.format(str2))
            pos = escolher_posicao_auto(tab, -1*jog, str2)
            tab = marcar_posicao(tab,-1*jog,pos)
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab) in [-1,1] or len(obter_posicoes_livres(tab))==0:
                break
            pos = escolher_posicao_manual(tab)               
            tab = marcar_posicao(tab,jog,pos)
            print(tabuleiro_str(tab)) 
            if jogador_ganhador(tab) in [-1,1] or len(obter_posicoes_livres(tab))==0:
                break
    
        if jogador_ganhador(tab) == 1:
            return 'X'
        elif jogador_ganhador(tab) == -1:
            return 'O'          
        else:
            return 'EMPATE'

#-----------------------------------------------------------------------------------------------#