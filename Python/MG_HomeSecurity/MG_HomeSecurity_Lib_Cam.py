# Cette Lib permet de gérer les échanges de données des caméra

# Class P (Parmeter) Sub of Class Z and F and Cam 
class P (): 
    
    def __init__(self):
        self.P1 = ""
        self.P2 = ""
        self.P3 = ""
        self.P4 = ""
        self.P5 = ""
        
# Class Z (Zone) Sub of Class F and Cam 
class Z (): 
    
    def __init__(self):
        self.Z1 = P() #Instance de P qui contient les 5 paramètres
        self.Z2 = P()
        self.Z3 = P()
        self.Z4 = P()
        
# Class F (Function) Sub of Class Cam       
class F (): 
    
    def __init__(self):
        self.F1 = Z() #Instance de Z qui contient les 4 zones et les 5 paramètres
        self.F2 = Z()
        self.F3 = Z()
        self.F4 = Z()      
        
# Class camera
class Camera ():

    #def __init__(self,setNumberOfID,setNumberOfZone,setNumberOfParameter):
    def __init__(self):
        
        # --- Abandon par tableau car l'appel par index n'est pas trés pratique ---##
        # self.setNumberOfID = setNumberOfID
        # self.setNumberOfZone = setNumberOfZone
        # self.setNumberOfParameter = setNumberOfParameter
        # matrix = [[["" for j in range(5)] for i in range(4)] for k in range(3)]
        # self.setting = [[["" for j in range(self.setNumberOfParameter)] for i in range(self.setNumberOfZone)] for k in range(self.setNumberOfID)]
        # matrix = [[["" for j in range(5)] for i in range(4)] for k in range(3)]
        # self.event = [[["" for j in range(self.setNumberOfParameter)] for i in range(self.setNumberOfZone)] for k in range(self.setNumberOfID)]
      
        # Variables reçues par la caméra
        self.Enable = "1"
        self.Setting = F() #Instance de F.Z.P
               
        # Variables envoyées par la caméra
        self.ClientName = "Cam"
        self.Event = F() #Instance de F.Z.P
        
        # Variable servant à la construction des messages d'échange via socket TCP
        self.MsgSend = ""
        self.MsgReceive = ""
        
        self.MsgSend_HMI = ""
        self.MsgReceive_HMI = ""

# Cam1 = Cam()
# Cam1.Setting.f1.z1.p1 = 123
# Cam1.Setting.f1.z1.p4 = 485

# print(Cam1)
# print(Cam1.Setting.f1.z1.p1)
# print(Cam1.Setting.f1.z1.p1)

#les variables suivantes commmunes pour la cam le serveur et l'ihm

# Instance Camera 1
Cam1 = Camera() 
Cam1.Enable = 1
Cam1.Setting.F1.Z1.P1 = 0.41 # threshold
Cam1.Setting.F1.Z1.P2 = "Aperson" # Filtre object_name
Cam1.Setting.F1.Z1.P3 = "23-33-103-153" # Interest box pt1x pt1y pt2x pt2y 
Cam1.ClientName = "Cam"
Cam1.Event.F1.Z1.P1 = "Person" # ObjectName
Cam1.Event.F1.Z1.P2 = 0.51 # Score
Cam1.Event.F1.Z1.P3 = "22-32-102-152" # Object detection box pt1x pt1y pt2x pt2y  
Cam1.MsgSend = ""
Cam1.MsgReceive = ""
Cam1.MsgSend_HMI = ""
Cam1.MsgReceive_HMI = ""

# Instance Camera 2
Cam2 = Camera() 
Cam2.Enable = 1
Cam2.Setting.F1.Z1.P1 = 0.32 # threshold
Cam2.Setting.F1.Z1.P2 = "Aperson" # Filtre object_name
Cam2.Setting.F1.Z1.P3 = "23-33-103-153" # Interest box pt1x pt1y pt2x pt2y 
Cam2.ClientName = "Cam"
Cam2.Event.F1.Z1.P1 = "Person" # ObjectName
Cam2.Event.F1.Z1.P2 = 0.42 # Score
Cam2.Event.F1.Z1.P3 = "22-32-102-152" # Object detection box pt1x pt1y pt2x pt2y  
Cam2.MsgSend = ""
Cam2.MsgReceive = ""
Cam2.MsgSend_HMI = ""
Cam2.MsgReceive_HMI = ""