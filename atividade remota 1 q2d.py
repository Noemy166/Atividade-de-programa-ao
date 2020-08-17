def quest2_d():
  return

def main(): 
  ah = int(input('Digite a hora: '))
  bm = int(input('Digite os minutos: '))
  cs = int(input('Digite os segundos: '))
  horas = ah * 3600
  minutos = bm * 60
  segundos = cs  
  resultado = horas + minutos + segundos
  print(f'Se passaram {resultado} segundos desde a meia-noite')

  
if __name__ == '__main__':
  main()
