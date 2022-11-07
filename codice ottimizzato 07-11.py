#Iniziamo con una schermata di benvenuto

print ("Salve utente, sono un assistente digitale che ti aiuterà con i tuoi compiti\n")
print ("Iniziamo nel chiederti quale compito vuoi eseguire:\n")

scelta=-1
while(scelta != 0):      #Inseriamo un while per la scelta dell'utente del menu
        print ("\nScegli cosa fare:")
        print ("1: Calcolo il perimetro di un quadrato\n2: Calcolo il perimetro di un cerchio\n3: Calcolo il perimetro di un rettangolo")
        print ("0: Esci dal programma\n")
        scelta=int(input(""))
        if (scelta == 0):
                print ("\nAlla prossima!")
                pass
        elif (scelta == 1):
                print ("\nInserisci la misura del lato del quadrato: ")
                lato_quadrato=int(input(""))
                print ("\nIl perimetro del tuo quadrato è: ", lato_quadrato*2, "\n\n")
        elif (scelta == 2):
                print ("\nInserisci il raggio del cerchio: ")
                raggio=int(input(""))
                print ("\nIl perimetro del tuo cerchio è: ", raggio*3.14*2, "\n\n")
        elif (scelta == 3):
                print ("\nInserisci la base del tuo rettangolo: ")
                base=int(input(""))
                print ("\nInserisci l'altezza: ")
                altezza=int(input(""))
                print ("\nIl perimetro del tuo rettangolo è: ", (base*2)+(altezza*2), "\n\n")
        else:
                print ("Non capisco")


#Ho implementato un ciclo if-elif-else sulla base delle scelte dell'utente.
#Così facendo il ciclo, dopo aver concluso ciascuna scelta riparte.
