
from insurancefirm import InsuranceFirm

class ReinsuranceFirm(InsuranceFirm):
    """ReinsuranceFirm class. 
       Inherits from InsuranceFirm."""
    def __init__(self, simulation, simulation_parameters, agent_parameters):
        """Constructor method.
               Accepts arguments
                   Signature is identical to constructor method of parent class.
           Constructor calls parent constructor and only overwrites boolean indicators of insurer and reinsurer role of 
           the object."""
        super(ReinsuranceFirm, self).__init__(simulation, simulation_parameters, agent_parameters)
        self.is_insurer = False
        self.is_reinsurer = True
