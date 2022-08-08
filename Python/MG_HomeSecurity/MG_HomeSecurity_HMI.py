# coding: utf-8

# Client HMI
import sys
import socket
import time
import threading
import matplotlib.pyplot as plt

from PyQt5 import QtWidgets
#from PyQt5.QtWidgets import QLineEdit
import MG_HomeSecurity_HMI_QT as Gui  # import du fichier gui.py généré par pyuic5

import MG_HomeSecurity_Lib_Cam as c

VarTest = 123

CloseApp_Flag = 0


class MyWindow(QtWidgets.QMainWindow):
    
    #def __init__(self, parent=None):
    def __init__(self, parent=None):
        
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Gui.Ui_MainWindow()
        self.ui.setupUi(self)
   
        # un clic sur le bouton appellera la méthode 'action_bouton'
        
        #self.ui.PBAcquittement.clicked.connect(self.Action_PBAcquittement)
        
        self.ui.PBAcquittement.clicked.connect(self.Action_PBAcquittement)
             
        self.ui.CBCam1Enable.clicked.connect(self.Action_CBCam1Enable)
        self.ui.CBCam2Enable.clicked.connect(self.Action_CBCam2Enable)
                
        #self.ui.LEC1SettingF1Z1P1.move(60, 60) 
        #self.ui.LEC1SettingF1Z1P1.textChanged.connect(self.textChanged_lineEdit)
        self.ui.LEC1SettingF1Z1P1.returnPressed.connect(self.returnPressed_lineEdit)
        #self.ui.LEC1SettingF1Z1P2.returnPressed.connect(self.returnPressed_lineEdit)
        #self.ui.LEC1SettingF1Z1P1.returnPressed.connect(lambda : self.returnPressed_lineEdit('LEC1SettingF1Z1P1'))
        #self.ui.LEC1SettingF1Z1P2.returnPressed.connect(lambda : self.returnPressed_lineEdit('LEC1SettingF1Z1P2'))

     
        
        #self.ui.actionQuitter.clicked.connect(self.Action__Quitter)
        self.ui.MMQuitter.triggered.connect(self.Action_MMQuitter)
        
      
        # on rempli la liste avec des chiffres
        #for i in range(20):
        #    self.ui.listWidget.addItem(str(i))

        # un clic sur un élément de la liste appellera la méthode 'on_item_changed'
        #self.ui.listWidget.currentItemChanged.connect(self.on_item_changed)

        # on affiche un texte en bas de la fenêtre (status bar)
        #self.ui.statusBar.showMessage("coucou")
 
        
    def Action_PBAcquittement(self):
        print("Action_PBAcquittement")
        
    def Action_CBCam1Enable(self): 
        cb = self.ui.CBCam1Enable         
        if self.ui.CBCam1Enable.isChecked() == True:
            print (self.ui.CBCam1Enable.text() + " is selected")
            c.Cam1.Enable = 1
        else:
            print (self.ui.CBCam1Enable.text()+" is deselected")
            c.Cam1.Enable = 0
        print("c.Cam1.Enable " , c.Cam1.Enable)
        
    def Action_CBCam2Enable(self): 
        cb = self.ui.CBCam2Enable         
        if self.ui.CBCam2Enable.isChecked() == True:
            print (self.ui.CBCam2Enable.text() + " is selected")
            c.Cam2.Enable = 1
        else:
            print (self.ui.CBCam2Enable.text()+" is deselected")
            c.Cam2.Enable = 0
        print("c.Cam2.Enable " , c.Cam2.Enable)

        
    def Action_MMQuitter(self):      
        global CloseApp_Flag   
        print("Close windows and bloc thread")
        CloseApp_Flag = 1
        self.close()
        
    def action_bouton(self):
        print('Appui bouton')

    def on_item_changed(self):
        print(self.ui.listWidget.currentItem().text())
        
    #def textChanged_lineEdit(self, text):
        #print (text)
        #pass
    def returnPressed_lineEdit(self):
        print(self.ui.LEC1SettingF1Z1P1.text())
        c.Cam1.Setting.F1.Z1.P1 = float(self.ui.LEC1SettingF1Z1P1.text())
        #print(self.ui.LEC1SettingF1Z1P1.text())
        #print(self.ui.LEC1SettingF1Z1P2.text())
        #print(self.ui.name.text())
        #print (name) 
        #setattr(self.data, name, value)
        
  
        
def Thread_socket ():
    
    global CloseApp_Flag 
 
    while CloseApp_Flag == 0 :
    
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", 1111))
                            
        #c.Cam1.Enable= input("Saisie ReceiveEnable_Cam1 >>")
        #ReceiveEnable_Cam1 = "1"
        #ReceiveConfig_Cam1 = "ModeTest"
        
        #MsgSend = ";" + ClientName + ";" + str(ReceiveEnable_Cam1) + ";" + str(ReceiveConfig_Cam1) + ";"     
        
        ##print("Cam1_Enable " , Cam1_Enable_state.get())  
        
        ##c.Cam1.Enable = Cam1_Enable_state.get()
        #c.Cam1.Enab  
                
        #c.Cam1.Setting.F1.Z1.P1 = Cam1_ConfigF1Z1P1_Txt.get()
        
        #Forçage
        ##c.Cam1.Setting.F1.Z1.P1 = 0.5
        c.Cam1.Setting.F1.Z1.P2 = "--person"
        
        c.Cam1.MsgSend = ";" + c.Cam1.ClientName + ";" + str(c.Cam1.Enable) + ";" + str(c.Cam1.Setting.F1.Z1.P1) + ";" \
            + c.Cam1.Setting.F1.Z1.P2 + ";" + c.Cam1.Setting.F1.Z1.P3 + ";"
            
            
        print("Cam1.MsgSend ", c.Cam1.MsgSend)
        #Msg = input('>> ')
        
        s.send(str(c.Cam1.MsgSend).encode())
        
        #file_name = 'data/%s' % (file_name,)
        r = s.recv(2048)
        
        c.Cam1.MsgReceive = str(r).split(";")
        ##print("Cam1.MsgReceive " , c.Cam1.MsgReceive) 
        #print("MsgReceive[1] " , MsgReceive[1] )
        
        c.Cam1.Event.F1.Z1.P1 = c.Cam1.MsgReceive[1]
        c.Cam1.Event.F1.Z1.P2 = c.Cam1.MsgReceive[2]
        c.Cam1.Event.F1.Z1.P3 = c.Cam1.MsgReceive[3]   
        
        ##L1_Txt.set(str(c.Cam1.MsgReceive[2]))
        ##E1_Txt.set(str(c.Cam1.MsgReceive[2]))
        
            
        
          
        #print("E1_Txt " , E1_Txt.get())
        #E1_Txt.set("789")
        
        #SendObjectName_Cam1 = MsgReceive[1]
        #Send_Score_Cam1 = MsgReceive[2]
        
        #print("Cam1.Event.F1.Z1.P1 " , c.Cam1.Event.F1.Z1.P1) # ObjectName
        #print("Cam1.Event.F1.Z1.P2 " , c.Cam1.Event.F1.Z1.P2) # Score 
        #print("Cam1.Event.F1.Z1.P3 " , c.Cam1.Event.F1.Z1.P3) # Object detection box pt1x pt1y pt2x pt2y
          
        #Cam1EventF1Z1P3 = str(r).split(":")
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
        
        
        
        time.sleep(1) #mini 1
        # Press 'q' to quit
        #print ("CloseApp_Flag" , CloseApp_Flag)
        # if BitClose == 1 :
        #     print ("Close")
        #     break

def Thread_socket2 ():
    
    global CloseApp_Flag 
 
    while CloseApp_Flag == 0 :
    
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", 1111))
                            
        #c.Cam1.Enable= input("Saisie ReceiveEnable_Cam1 >>")
        #ReceiveEnable_Cam1 = "1"
        #ReceiveConfig_Cam1 = "ModeTest"
        
        #MsgSend = ";" + ClientName + ";" + str(ReceiveEnable_Cam1) + ";" + str(ReceiveConfig_Cam1) + ";"     
        
        ##print("Cam1_Enable " , Cam1_Enable_state.get())  
        
        ##c.Cam1.Enable = Cam1_Enable_state.get()
        #c.Cam1.Enab  
                
        ##c.Cam1.Setting.F1.Z1.P1 = Cam1_ConfigF1Z1P1_Txt.get()
        
        c.Cam2.MsgSend = ";" + c.Cam2.ClientName + ";" + str(c.Cam2.Enable) + ";" + str(c.Cam2.Setting.F1.Z1.P1) + ";" \
            + c.Cam2.Setting.F1.Z1.P2 + ";" + c.Cam2.Setting.F1.Z1.P3 + ";"
            
            
        print("Cam2.MsgSend ", c.Cam2.MsgSend)
        #Msg = input('>> ')
        
        s.send(str(c.Cam2.MsgSend).encode())
        
        #file_name = 'data/%s' % (file_name,)
        r = s.recv(2048)
        
        c.Cam2.MsgReceive = str(r).split(";")
        ##print("Cam2.MsgReceive " , c.Cam2.MsgReceive) 
        #print("MsgReceive[1] " , MsgReceive[1] )
        
        c.Cam2.Event.F1.Z1.P1 = c.Cam2.MsgReceive[1]
        c.Cam2.Event.F1.Z1.P2 = c.Cam2.MsgReceive[2]
        c.Cam2.Event.F1.Z1.P3 = c.Cam2.MsgReceive[3]   
        
        ##L1_Txt.set(str(c.Cam1.MsgReceive[2]))
        ##E1_Txt.set(str(c.Cam1.MsgReceive[2]))
        
            
        
          
        #print("E1_Txt " , E1_Txt.get())
        #E1_Txt.set("789")
        
        #SendObjectName_Cam1 = MsgReceive[1]
        #Send_Score_Cam1 = MsgReceive[2]
        
        #print("Cam1.Event.F1.Z1.P1 " , c.Cam1.Event.F1.Z1.P1) # ObjectName
        #print("Cam1.Event.F1.Z1.P2 " , c.Cam1.Event.F1.Z1.P2) # Score 
        #print("Cam1.Event.F1.Z1.P3 " , c.Cam1.Event.F1.Z1.P3) # Object detection box pt1x pt1y pt2x pt2y
          
        #Cam1EventF1Z1P3 = str(r).split(":")
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
        # Press 'q' to quit
        #print ("CloseApp_Flag" , CloseApp_Flag)
        # if BitClose == 1 :
        #     print ("Close")
        #     break
         

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


c.Cam1.ClientName = "HMI_CAM1"
#c.Cam1.Enable = input("Saisie Cam1.Enable >>")
c.Cam1.Enable = 1 # Active à cam au boot
#c.Cam1.Setting.F1.Z1.P1 = 0.35 # threshold
c.Cam1.Setting.F1.Z1.P2 = "---person" # Filtre object_name
c.Cam1.Setting.F1.Z1.P3 = ":21:31:101:151:" # Interest box pt1x pt1y pt2x pt2y 

c.Cam2.ClientName = "HMI_CAM2"
#c.Cam1.Enable = input("Saisie Cam1.Enable >>")
c.Cam2.Enable = 1 # Active à cam au boot
#c.Cam1.Setting.F1.Z1.P1 = 0.35 # threshold
c.Cam2.Setting.F1.Z1.P2 = "---person" # Filtre object_name
c.Cam2.Setting.F1.Z1.P3 = ":21:31:101:151:" # Interest box pt1x pt1y pt2x pt2y 



#c.Cam1.Enable= input("Saisie ReceiveEnable_Cam1 _ >>")



if __name__ == '__main__':
    
    Thread_socket_1 = threading.Thread(target=Thread_socket)
    print("Start -> Thread_socket ") 
    Thread_socket_1.start()
    
    Thread_socket_2 = threading.Thread(target=Thread_socket2)
    print("Start -> Thread_socket 2 ") 
    Thread_socket_2.start()
    
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    print("Start -> QT Window ")
    sys.exit(app.exec_())
   





    

    
    



