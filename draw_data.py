from dataclasses import dataclass
from random import randint

@dataclass
class DrawData:
   name: str
   full_name: str
   gens: int
   axiom: str
   chr_1: str
   rule_1: str
   chr_2: str
   rule_2: str
   draw_color: str
   angle: int