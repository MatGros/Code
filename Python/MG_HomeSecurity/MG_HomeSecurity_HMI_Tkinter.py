# coding: utf-8

# Client HMI

import socket
import time
import threading
import matplotlib.pyplot as plt
from tkinter import *

import MG_HomeSecurity_Lib_Cam as c

VarTest = 123

def callback(): 
    E1_Txt.set("plop")
    print("plop")
    
def callback2(): 
    global VarTest
    VarTest = VarTest + 1
    print("plop 2 " , VarTest) 

def Cam1_Enable(): 
    #Cam1_Enable.toggle()
    print("Cam1_Enable ") 


fenetre = Tk()
fenetre.title("Titre")
fenetre.geometry
fenetre.geometry("800x500")
fenetre.resizable(width=1, height=1)

# Titre CAM fixe
Cam1_Titre = Label(fenetre, text="CAM1")
Cam1_Titre.place(x=10, y=10, width=50, height=25)

# CheckBox Enable
Cam1_Enable_state = StringVar()
Cam1_Enable_state.set(1) # Init 
Cam1_Enable = Checkbutton(fenetre, text="Enable", variable=Cam1_Enable_state, command=Cam1_Enable)
Cam1_Enable.place(x=0, y=35, width=100, height=25)

# EntryBox threshold
Cam1_ConfigF1Z1P1_Txt = StringVar()
Cam1_ConfigF1Z1P1_Txt.set(0.35) # Init
Cam1_ConfigF1Z1P1 = Entry(fenetre, textvariable=Cam1_ConfigF1Z1P1_Txt, width=30)
Cam1_ConfigF1Z1P1.place(x=50, y=60, width=100, height=25) 


L1_Txt = StringVar()
L1 = Label(fenetre, textvariable=L1_Txt)
L1.place(x=295, y=55, width=50, height=25)

B1 = Button(fenetre, text="B1", command=callback)
B1.place(x=95, y=55, width=50, height=25)

B2 = Button(fenetre, text="B2", command=callback2)
B2.place(x=195, y=55, width=50, height=25) 

L2 = Label(fenetre, text="L2")
L2.place(x=395, y=55, width=150, height=25) 

E1_Txt = StringVar()
E1_Txt.set('E1')
E1 = Entry(fenetre, textvariable=E1_Txt, width=30)
E1.place(x=495, y=55, width=150, height=25) 



def Thread_socket ():
    
      
    
    while True :
    
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", 1111))
                            
        #c.Cam1.Enable= input("Saisie ReceiveEnable_Cam1 >>")
        #ReceiveEnable_Cam1 = "1"
        #ReceiveConfig_Cam1 = "ModeTest"
        
        #MsgSend = ";" + ClientName + ";" + str(ReceiveEnable_Cam1) + ";" + str(ReceiveConfig_Cam1) + ";"     
        
        print("Cam1_Enable " , Cam1_Enable_state.get())  
        
        c.Cam1.Enable = Cam1_Enable_state.get()
        c.Cam1.Setting.F1.Z1.P1 = Cam1_ConfigF1Z1P1_Txt.get()
        
        c.Cam1.MsgSend = ";" + c.Cam1.ClientName + ";" + str(c.Cam1.Enable) + ";" + str(c.Cam1.Setting.F1.Z1.P1) + ";" \
            + c.Cam1.Setting.F1.Z1.P2 + ";" + c.Cam1.Setting.F1.Z1.P3 + ";"
            
            
        print("Cam1.MsgSend ", c.Cam1.MsgSend)
        #Msg = input('>> ')
        
        s.send(str(c.Cam1.MsgSend).encode())
        
        #file_name = 'data/%s' % (file_name,)
        r = s.recv(2048)
        
        c.Cam1.MsgReceive = str(r).split(";")
        print("Cam1.MsgReceive " , c.Cam1.MsgReceive) 
        #print("MsgReceive[1] " , MsgReceive[1] )
        
        c.Cam1.Event.F1.Z1.P1 = c.Cam1.MsgReceive[1]
        c.Cam1.Event.F1.Z1.P2 = c.Cam1.MsgReceive[2]
        c.Cam1.Event.F1.Z1.P3 = c.Cam1.MsgReceive[3]   
        
        L1_Txt.set(str(c.Cam1.MsgReceive[2]))
        E1_Txt.set(str(c.Cam1.MsgReceive[2]))
        
            
        
          
        #print("E1_Txt " , E1_Txt.get())
        #E1_Txt.set("789")
        
        #SendObjectName_Cam1 = MsgReceive[1]
        #Send_Score_Cam1 = MsgReceive[2]
        
        #print("Cam1.Event.F1.Z1.P1 " , c.Cam1.Event.F1.Z1.P1) # ObjectName
        #print("Cam1.Event.F1.Z1.P2 " , c.Cam1.Event.F1.Z1.P2) # Score 
        #print("Cam1.Event.F1.Z1.P3 " , c.Cam1.Event.F1.Z1.P3) # Object detection box pt1x pt1y pt2x pt2y
          
        Cam1EventF1Z1P3 = str(r).split(":")
        #print("Cam1EventF1Z1P3[1] " , Cam1EventF1Z1P3[1])
        #print("Cam1EventF1Z1P3[2] " , Cam1EventF1Z1P3[2])
        #print("Cam1EventF1Z1P3[3] " , Cam1EventF1Z1P3[3])
        #print("Cam1EventF1Z1P3[4] " , Cam1EventF1Z1P3[4])
        
        #x = [1, 0, -1, 0, 1]
        #y = [0, 1, 0, -1, 0]
        #x = [Cam1EventF1Z1P3[1], Cam1EventF1Z1P3[3]]
        #y = [Cam1EventF1Z1P3[2], Cam1EventF1Z1P3[4]]
        #plt.plot(x, y)
        #plt.xlim(-10, 10)
        #plt.ylim(-10, 10)
        #plt.show()
        time.sleep(1)


         


# Cam1 = Cam() #Instance Cam
# Cam1.Enable = 1
# Cam1.Setting.F1.Z1.P1 = 0.35 # threshold1
# Cam1.Setting.F1.Z1.P2 = "Aperson" # Filtre object_name
# Cam1.Setting.F1.Z1.P3 = "20-30-100-150" # Interest box pt1x pt1y pt2x pt2y 
# Cam1.ClientName = "Cam1"
# Cam1.Event.F1.Z1.P1 = "" # ObjectName
# Cam1.Event.F1.Z1.P2 = "" # Score
# Cam1.Event.F1.Z1.P3 = "" # Object detection box pt1x pt1y pt2x pt2y  
# Cam1.MsgSend = ""
# Cam1.MsgReceive = ""


c.Cam1.ClientName = "HMI"
#c.Cam1.Enable = input("Saisie Cam1.Enable >>")
#c.Cam1.Enable = 1 # Active à cam au boot
#c.Cam1.Setting.F1.Z1.P1 = 0.35 # threshold
c.Cam1.Setting.F1.Z1.P2 = "---person" # Filtre object_name
c.Cam1.Setting.F1.Z1.P3 = ":21:31:101:151:" # Interest box pt1x pt1y pt2x pt2y 




#c.Cam1.Enable= input("Saisie ReceiveEnable_Cam1 _ >>")



Thread_socket_1 = threading.Thread(target=Thread_socket)
print("Start -> Thread_socket ") 
Thread_socket_1.start()

print("Start -> mainloop() ") 
fenetre.mainloop()






    

    
    



