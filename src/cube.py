import utils

class Cubit: 
    def __init__(self: Cubit, is_corner: bool, face_colors: list[Color], permutation: int, orientation: int) {
        self.is_cornner: bool = is_corner           # True if Cubit is a corner, False if Cubit is an edge.
        self.face_colors: list[Color] = face_colors # len(list) = 3 for corners, 2 for edges. Describes the colors of cubits faces. 
        self.permutation: int = permutation         # int corresponding to index in edges/corners attribute in Cube class. 
        self.orientation: int = orientation         # int corresponding to index in edges/corners attribute in Cube class. 
    }

class Cube:
    def __init__(self: Cube) {
        self.corners: list[Cubit]   # len(list) = 8. ALl Cubit instances has is_corner = True. 
        self.edges: list[Cubit]     # len(list) = 12. All Cubit instances has is_corner = False. 
        self.rotation: int = 0      # Integer from 0 to 24. 90deg rotations around x,y,z axes only.
    }

