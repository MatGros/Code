# coding: utf-8 

# Server

import socket
import threading
from datetime import datetime

import MG_HomeSecurity_Lib_Cam as c

#Variables socket client
MsgSendHMI= ""

#ClientName_Cam1, ReceiveEnable_Cam1, ReceiveConfig_Cam1, SendObjectName_Cam1, Send_Score_Cam1 = "" , "" , "" , "" , "" ,
#MsgSendCam1 = ""

Client2_Variable1 = 0
Client2_Variable2 = 0

Client3_Variable1 = 0
Client3_Variable2 = 0

TestEnableClient2 = 789
    

class ClientThread(threading.Thread):
        
    
        
    def __init__(self, ip, port, clientsocket):
         
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))


    def run(self):
    
        #Déclaration des variables globables qui seront échangés entre les clients clients
        global TestEnableClient2
        #Passen global les varaibles devants être échangées avec le programme de gestion ou les autres clients
        global ReceiveEnable_Cam1, ReceiveConfig_Cam1, SendObjectName_Cam1, Send_Score_Cam1
        
        print("Connexion de %s %s" % (self.ip, self.port, ))
        
        r = self.clientsocket.recv(2048)
        #print("clientsocket.recv " , r)
        
        MsgReceive = str(r).split(";")
        #print("MsgReceive[1] " , MsgReceive[1] )
        

         
        if MsgReceive[1] == "HMI_CAM1" :
            
            c.Cam1.Enable = MsgReceive[2]
            c.Cam1.Setting.F1.Z1.P1 = MsgReceive[3]
            c.Cam1.Setting.F1.Z1.P2 = MsgReceive[4]
            c.Cam1.Setting.F1.Z1.P3 = MsgReceive[5]
            print("Cam1.Enable " , c.Cam1.Enable)
            print("Cam1.Setting.F1.Z1.P1 " , c.Cam1.Setting.F1.Z1.P1)
            print("Cam1.Setting.F1.Z1.P2 " , c.Cam1.Setting.F1.Z1.P2) 
            print("Cam1.Setting.F1.Z1.P3 " , c.Cam1.Setting.F1.Z1.P3) 
            
            c.Cam1.MsgSend_HMI = ";" + str(c.Cam1.Event.F1.Z1.P1) + ";" + str(c.Cam1.Event.F1.Z1.P2) + ";" + str(c.Cam1.Event.F1.Z1.P3) + ";"
            #("Cam1.MsgSend " , Cam1.MsgSend)
            self.clientsocket.send(str(c.Cam1.MsgSend_HMI).encode())
            
            #ReceiveEnable_Cam1 = MsgReceive[2]
            #ReceiveConfig_Cam1 = MsgReceive[3]
            #print("ReceiveEnable_Cam1 " , ReceiveEnable_Cam1)
            #print("ReceiveConfig_Cam1 " , ReceiveConfig_Cam1)
            
            #MsgSendHMI= ";" + str(SendObjectName_Cam1) + ";" + str(Send_Score_Cam1) + ";"
            #print("MsgSendHMI " , MsgSendHMI)
            #self.clientsocket.send(str(MsgSendHMI).encode())
            
        if MsgReceive[1] == "HMI_CAM2" :
            
            c.Cam2.Enable = MsgReceive[2]
            c.Cam2.Setting.F1.Z1.P1 = MsgReceive[3]
            c.Cam2.Setting.F1.Z1.P2 = MsgReceive[4]
            c.Cam2.Setting.F1.Z1.P3 = MsgReceive[5]
            print("Cam2.Enable " , c.Cam2.Enable)
            print("Cam2.Setting.F1.Z1.P1 " , c.Cam2.Setting.F1.Z1.P1)
            print("Cam2.Setting.F1.Z1.P2 " , c.Cam2.Setting.F1.Z1.P2) 
            print("Cam2.Setting.F1.Z1.P3 " , c.Cam2.Setting.F1.Z1.P3) 
            
            c.Cam2.MsgSend_HMI = ";" + str(c.Cam2.Event.F1.Z1.P1) + ";" + str(c.Cam2.Event.F1.Z1.P2) + ";" + str(c.Cam2.Event.F1.Z1.P3) + ";"
            #("Cam2.MsgSend " , Cam2.MsgSend)
            self.clientsocket.send(str(c.Cam2.MsgSend_HMI).encode())
            
            #ReceiveEnable_Cam1 = MsgReceive[2]
            #ReceiveConfig_Cam1 = MsgReceive[3]
            #print("ReceiveEnable_Cam1 " , ReceiveEnable_Cam1)
            #print("ReceiveConfig_Cam1 " , ReceiveConfig_Cam1)
            
            #MsgSendHMI= ";" + str(SendObjectName_Cam1) + ";" + str(Send_Score_Cam1) + ";"
            #print("MsgSendHMI " , MsgSendHMI)
            #self.clientsocket.send(str(MsgSendHMI).encode()) 
            
        if MsgReceive[1] == "CAM1" :
            
            c.Cam1.Event.F1.Z1.P1 = MsgReceive[2]
            c.Cam1.Event.F1.Z1.P2 = MsgReceive[3]
            c.Cam1.Event.F1.Z1.P3 = MsgReceive[4]
            #print("Cam1.Event.F1.Z1.P1 " , c.Cam1.Event.F1.Z1.P1)
            #print("Cam1.Event.F1.Z1.P2 " , c.Cam1.Event.F1.Z1.P2)
            #print("Cam1.Event.F1.Z1.P3 " , c.Cam1.Event.F1.Z1.P3)
            
            c.Cam1.MsgSend = ";" + str(c.Cam1.Enable) + ";" + str(c.Cam1.Setting.F1.Z1.P1) + ";" + str(c.Cam1.Setting.F1.Z1.P2) + ";"  + str(c.Cam1.Setting.F1.Z1.P3) + ";"
            #print("Cam1.MsgSend " , Cam1.MsgSend )
            self.clientsocket.send(str(c.Cam1.MsgSend).encode())
            
            # SendObjectName_Cam1 = MsgReceive[2]
            # Send_Score_Cam1 = MsgReceive[3]
            # print("SendObjectName_Cam1 " , SendObjectName_Cam1)
            # print("Send_Score_Cam1 " , Send_Score_Cam1)
            
            # MsgSendCam1 = ";" + str(ReceiveEnable_Cam1) + ";" + str(ReceiveConfig_Cam1) + ";"
            # print("MsgSendCam1 " , MsgSendCam1 )
            # self.clientsocket.send(str(MsgSendCam1).encode())
            
        
        if MsgReceive[1] == "CAM2" :
            
            c.Cam2.Event.F1.Z1.P1 = MsgReceive[2]
            c.Cam2.Event.F1.Z1.P2 = MsgReceive[3]
            c.Cam2.Event.F1.Z1.P3 = MsgReceive[4]
            # print("Cam2.Event.F1.Z1.P1 " , c.Cam2.Event.F1.Z1.P1)
            # print("Cam2.Event.F1.Z1.P2 " , c.Cam2.Event.F1.Z1.P2)
            # print("Cam2.Event.F1.Z1.P3 " , c.Cam2.Event.F1.Z1.P3)
            
            c.Cam2.MsgSend = ";" + str(c.Cam2.Enable) + ";" + str(c.Cam2.Setting.F1.Z1.P1) + ";" + str(c.Cam2.Setting.F1.Z1.P2) + ";"  + str(c.Cam2.Setting.F1.Z1.P3) + ";"
            #print("Cam2.MsgSend " , Cam2.MsgSend )
            self.clientsocket.send(str(c.Cam2.MsgSend).encode())
            
            
        if MsgReceive[1] == "Client3" :
            
            Client3_Variable1 = MsgReceive[2]
            Client3_Variable2 = MsgReceive[3]
            print("Client3_Variable1 " , Client3_Variable1)
            print("Client3_Variable2 " , Client3_Variable2)
            
            TestEnableClient2 = Client3_Variable1
            self.clientsocket.send(str(TestEnableClient2).encode())

            
            
                
        #print(string.split(r,";"))
        #print("Ouverture du fichier: ", r, "...")
        #fp = open(r, 'rb')
        #self.clientsocket.send(fp.read())

        #print("Client déconnecté...")



tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("127.0.0.1",1111))

# Cam1 = Cam() #Instance Cam
# Cam1.Enable = 0
# Cam1.Setting.F1.Z1.P1 = 0 # threshold
# Cam1.Setting.F1.Z1.P2 = "" # Filtre object_name
# Cam1.Setting.F1.Z1.P3 = "" # Interest box pt1x pt1y pt2x pt2y 
# Cam1.ClientName = ""
# Cam1.Event.F1.Z1.P1 = "" # ObjectName
# Cam1.Event.F1.Z1.P2 = "" # Score
# Cam1.Event.F1.Z1.P3 = "" # Object detection box pt1x pt1y pt2x pt2y 
# Cam1.MsgSend = ""
# Cam1.MsgReceive = ""


while True:
    
    #TestEnableClient2 = TestEnableClient2 +1 
    tcpsock.listen(10)
    print( "En écoute...\n")
    DateStart = datetime.now()
    #print("Now : " , datetime.now())
    
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()
    #print("Cycle : " , datetime.now()-DateStart)
    
    #print("---------------SendObjectName_Cam1 " , SendObjectName_Cam1)
    #print("---------------ReceiveConfig_Cam1 " , ReceiveConfig_Cam1)
    #print("---------------ReceiveEnable_Cam1 " , ReceiveEnable_Cam1)
