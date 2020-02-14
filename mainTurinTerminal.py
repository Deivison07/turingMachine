# A Primeira Instrução tem que começar com "Q0"!
lista = ['1','0','0','0','0','0','B','fim']


dicionario['QF,*'] = '0','0','0'
dicionario['Q0,1'] = 'Q1','1','D'
dicionario['Q1,1'] = 'Q1','1','D'
dicionario['Q1,0'] = 'Q3','0','D'
dicionario['Q3,0'] = 'Q3','0','D'
dicionario['Q3,B'] = 'QF','B','E'

dicionario = {}
index = 0

ponteiro = 'Q0,'+lista[0]
letra = lista[index]

def controle():
    
    global ponteiro,letra,dicionario,lista,index

    if  ponteiro.split(',')[0] == 'QF':
        print("Programa Finalisou com susseso ")
    else:
        if ponteiro in dicionario.keys():
            if dicionario[ponteiro][2] == 'D':
                
                lista[index] = dicionario[ponteiro][1]
                index = index + 1 
                try:
                    ponteiro = str(dicionario[ponteiro][0]+','+lista[index])
                except:
                    print('Ponteiro Fora Da Fita Erro Fatal!')
                
            else: 
                
                if dicionario[ponteiro][2] == 'E' and index > 0:
                    lista[index] = dicionario[ponteiro][1]
                    index = index - 1 
                    ponteiro = str(dicionario[ponteiro][0]+','+lista[index])
                else:
                    print('ponteiro fora da Fita Erro Fatal!')
        
            print(ponteiro)
            print(lista)
        else:
            print("Este ponteiro nao existe! Fim de programa!")
            
while(1):
    controle()
    if input():
        pass
    else:
        break
    
