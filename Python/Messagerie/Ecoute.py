#!/usr/bin/python
# -*- coding: latin-1 -*-
import socket      # importe un ensemble d'instructions pour connecter les programmes.
                   # Cet ensemble est disponible a l'installation de Python, dans la bibliotheque de base.
 
# Creation du connecteur d'ecoute par l'instruction 'socket' 
# de la bibliotheque socket precedemment importee.
Connecteur = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
Hote = '127.0.0.1' # Adresse locale de l'ordinateur.
Port = 80          # Choix d'un port d'ecoute.
Connecteur.bind((Hote,Port)) # instruction 'bind' de la bibliotheque du connecteur
print ("Le programme est a l'ecoute d'une eventuelle discussion, vous en serez averti.") # Rajoutez des parentheses pour Python 3 !
Connecteur.listen(1)                  # ecoute...
client, adresse = Connecteur.accept() # accepte...
print ("L'ordinateur",adresse," veut discuter ! J'attends son message.") # Rajoutez des parentheses pour Python 3 !
 
# Creation du connecteur de reponse
Reponse = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Portreponse = 234
Reponse.connect((Hote,Portreponse ))
print ("Note : je me suis connecte a",adresse," pour lui repondre") # Rajoutez des parentheses pour Python 3 !
 
while 1:
        Message = client.recv(255) # reception de la reponse, 255 caracteres max ; Python 3 : Message = str(client.recv(255),'mac_roman')
        if not Message: 
                break  
        print ("\nMessage : ",Message,"\a" + "\n\nVotre reponse :") # Rajoutez des parentheses pour Python 3 !
        msgR = bytes(input('>> '), 'mac_roman')   # votre message ? Python 3 : msgR = bytes(input('>> '), 'mac_roman')
        Reponse.send(msgR)        # envoi. 
 
client.close() # ferme la connexion lorsque le client est parti : [ctrl+C] pour abandonner l'execution du programme.
