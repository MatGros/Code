#!/usr/bin/python
# -*- coding: latin-1 -*-
import socket
Discuter = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Hote = '127.0.0.1'
Port = 80
Port_de_reponse = 234
Discuter.connect((Hote,Port))       # Se connecte au programme ecoute.py
 
Reponse = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Reponse.bind((Hote,Port_de_reponse))
Reponse.listen(1)
client, adresse = Reponse.accept()  # Creation du connecteur pour la reponse de ecoute.py
print ("L'adresse",adresse," vous a entendu et attend votre message.") # Rajoutez des parentheses pour Python 3 !
while 1:
        msg = bytes(input('>> '), 'mac_roman')  # votre message ? Python 3 : msg = bytes(input('>> '), 'mac_roman')
        Discuter.send(msg)      # envoi.
        print ("Attente de la reponse...") # Rajoutez des parentheses pour Python 3 !
        reponseaumessage = client.recv(255) # reception de la reponse, 255 caracteres max ; Python 3 : reponseaumessage = str(client.recv(255),'mac_roman')
        if not reponseaumessage:
                break  
        print ("\n",adresse,":",reponseaumessage,"\a\n")  # affiche la reponse # Rajoutez des parentheses pour Python 3 !
 
client.close() # ferme la connexion lorsque le client quitte.