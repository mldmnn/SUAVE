## @ingroup Methods-Aerodynamics-Higher_Fidelity-Drag
# untrimmed.py
#
# Created:  Jan 2014, T. Orra
# Modified: Jun 2017, T. MacDonald  

# ----------------------------------------------------------------------
#  Untrimmed
# ----------------------------------------------------------------------

## @ingroup Methods-Aerodynamics-Higher_Fidelity-Drag
def untrimmed(state,settings,geometry):
    """ This computes the total drag of an aircraft without trim
    and stores that data in the conditions structure.

    Assumptions:
    None

    Source:
    N/A

    Inputs:
    state.conditions.aerodynamics.drag_breakdown.
      parasite.total                               [Unitless]
      induced.total                                [Unitless]
      compressible.total                           [Unitless]
      miscellaneous.total                          [Unitless]

    Outputs:
    aircraft_untrimmed                             [Unitless]

    Properties Used:
    N/A
    """      

    # Unpack inputs
    conditions     = state.conditions
    configuration  = settings
    drag_breakdown = conditions.aerodynamics.drag_breakdown

    # Various drag components
    compressibility_total = conditions.aerodynamics.drag_breakdown.compressible.total    
    induced_total         = conditions.aerodynamics.drag_breakdown.induced.total  
    invisid_total         = compressibility_total + induced_total
    parasite_total        = conditions.aerodynamics.drag_breakdown.parasite.total              
    miscellaneous_drag    = conditions.aerodynamics.drag_breakdown.miscellaneous.total 

    # Untrimmed drag
    aircraft_untrimmed = invisid_total        \
        + parasite_total \
        + miscellaneous_drag
    
    conditions.aerodynamics.drag_breakdown.untrimmed = aircraft_untrimmed
    
    return aircraft_untrimmed