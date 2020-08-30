def sinal(cor):
    if cor == 'V':
        return f'('Siga')
    elif cor == 'A':
        return f'('Atenção')
        elif cor == 'E':
        return f'('Pare')
   
def main():
   c = str(input('''Qual o a cor do semaforo
   V = verde
   A = amarelo
   E = vermelho'''))
   fazer = sinal(cor)
print(fazer)
if__name__ =='__main__':
    main()