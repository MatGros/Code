import socket
from datetime import datetime

from MG_HomeSecurity_Lib_Cam import Camera

#c = Camera()

class SocketCam:
      
    #def __init__(self,ClientName,ReceiveConfig,SendObjectName,Send_Score):
    # En paramètre tous ce qui va être envoyé au server    
    def __init__(self,):  
        # Instance structure
        self.ClientName = ""
        self.EventF1Z1P1 = ""
        self.EventF1Z1P2 = ""
        self.EventF1Z1P3 = ""
        
    def RW(self):   

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", 1111))
        
    
        #MsgSend = ";" + ClientName + ";" + str(SendObjectName) + ";" + str(Send_Score) + ";" 
        MsgSend = ";" + self.ClientName + ";" + str(self.EventF1Z1P1) + ";" + str(self.EventF1Z1P2) + ";" + str(self.EventF1Z1P3) + ";"
    
        #MsgSendSplit = MsgSend.split(";")
        #print(MsgSendSplit)
        #print(MsgSendSplit[0])
        #print(MsgSendSplit[1])
    
        print("MsgSend :", MsgSend)
        #Msg = input('>> ')
    
        s.send(MsgSend.encode())
    
        r = s.recv(2048)
        print("r:", r)
        
        MsgReceive = str(r).split(";")
        
        #print("MsgReceive " , MsgReceive) 
        #print("MsgReceive[1] " , MsgReceive[1] )
          
        self.Enable = MsgReceive[1]
        self.SettingF1Z1P1 = MsgReceive[2]
        self.SettingF1Z1P2 = MsgReceive[3] 
        self.SettingF1Z1P3 = MsgReceive[4]

        