h = 0 #horas  #23:55:58 -> ALARME!!!
while h < 24:
    m = 0 #minutos
    while m < 60:
        s = 0 #segundos
        while s < 60:
            print(f'{h:02}:{m:02}:{s:02}')
            if h == 23 and m == 55 and s == 58:
                print('ALARME!!!')
                break
            s+=1
        if h == 23 and m == 55:
           break
        m+=1
    if h == 23:
        break
    h+=1


ha = int(input('Hora: '))
ma = int(input('Minuntos: '))
sa = int(input('Segundos: '))

h = 0 #horas
while h < 24:
    m = 0 #minutos
    while m < 60:
        s = 0 #segundos
        while s < 60:
            print(f'{h:02}:{m:02}:{s:02}')
            if h == ha and m == ma and s == sa:
                print('ALARME!!!')
                break
            s+=1
        if h == ha and m == ma:
            break
        m+=1
    if h == ha:
        break
    h+=1
