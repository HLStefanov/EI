#https://www.panasonic-electric-works.com/cps/rde/xbcr/pew_eu_en/ca_pir_motionsensors_1192_en.pdf

class Sensor:



    def __init__(self,dtype,name,detection_zones,detection_distance,view_x,view_y):
        self.dtype = dtype
        self.name = 'WADT'  # stands for Wide Area Detection Type
        self.detection_distance = detection_distance
        self.detection_zones = 3.0
        self.view_x = 130
        self.view_y = 130

    def set_detection_distance(self,detection_distance):
        self.__detection_distance = detection_distance
    
    def set_name(self,name):
        self.__name = name

    def set_view_x(self,view_x):
        self.__view_x = view_x

    def set_view_y(self,view_y):
        self.__view_y= view_y     