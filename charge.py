from constants import Constants
import numpy as np

class Charge:
  def __init__(self, charge, position = np.zeros(2), velocity = np.zeros(2)):
    '''
    charge: charge of the particle in Coulombs
    position: 3D numpy array for position vector
    velocity: 3D numpy array for velocity vector
    '''
    self.charge = charge * Constants.E
    self.mass = Constants.MASS_ELECTRON
    self.position = position
    self.prevPosition = np.zeros(2)
    self.velocity = velocity
  


    
    



  
