"""
T O D O list
Mark outliers of CEMBA data
Annotate the major type of CEMBA data
Multi-round clustering of CEMBA data

For each dataset, write a get gene value function, given gene name, return gene value, cache genes

"""

from .aibs import aibs
from .annot import AIBSTENXCellAnnotation, AIBSSMARTCellAnnotation, BROADTENXCellAnnotation
from .brain_region import brain
from .broad import broad
from .cemba import cemba
from .genome import mm10
