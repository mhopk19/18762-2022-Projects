import numpy as np
from itertools import count
from classes.Nodes import Nodes
# from lib.stamping_functions import stamp_y_sparse, stamp_j_sparse

class VoltageSources:
    def __init__(self, name, vp_node, vn_node, amp_ph_ph_rms, phase_deg, frequency_hz):
        self.name = name
        self.vp_node = vp_node
        self.vn_node = vn_node
        self.amp_ph_ph_rms = amp_ph_ph_rms
        self.phase_deg = phase_deg
        self.frequency_hz = frequency_hz
        self.ecm_type = ""
        self.ecm_val = 0
        # You are welcome to / may be required to add additional class variables   

    def get_nom_voltage(self):
        return self.amp_ph_ph_rms
    
    # Some suggested functions to implement, 
    def assign_node_indexes(self,):
        pass
        
    def stamp_sparse(self,):
        pass

    def stamp_dense(self,):
        pass

    def stamp_open(self,):
        pass
    
    def __str__(self):
        return "V-{}-{}".format(self.amp_ph_ph_rms, id(self))
    
    def __repr__(self):
        return self.__str__()
        
