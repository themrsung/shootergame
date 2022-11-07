import sys
sys.path.insert(1, "/classes")

from classes.level import *
from classes.object import *
from classes.pawn import *
from classes.weapon import *

from classes.weapons.rifles import *
from classes.weapons.pistols import *

level = Level(
    [
        Pawn(PawnData(
            100,
            100,
            0,
            0,
            Armalite()
        )
        ),
        Pawn(PawnData(
            200,
            200,
            0,
            0,
            Glock()
        ))
    ]
)

for object in level.objects:
    print(object)