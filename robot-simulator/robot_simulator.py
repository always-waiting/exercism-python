class Direction(object):
    direction = []
    def __new__(cls, direction):
        if not direction in ["N", "E", "S", "W"]: raise ValueError
        if len(direction) == 0: direction.append(object.__new__(cls, direction))
        for obj in Direction.direction:
            if obj.direction == direction:
                return obj
        Direction.direction.append(object.__new__(cls, direction))
        return Direction.direction[-1]

    def __init__(self, direction):
        self.direction = direction

    def turn_right(self):
        index = Direction.direction.index(self)
        return Direction.direction[(index + 1) % 4]
    def turn_left(self):
        index = Direction.direction.index(self)
        return Direction.direction[(index - 1) % 4]



NORTH = Direction("N")
EAST = Direction("E")
SOUTH = Direction("S")
WEST = Direction("W")

class Robot(object):
    def __init__(self, direction=NORTH, x=0, y=0):
        self.x = x
        self.y = y
        self.bearing = direction

    @property
    def coordinates(self):
        return (self.x, self.y
                )
    def turn_right(self):
        self.bearing = self.bearing.turn_right()

    def turn_left(self):
        self.bearing = self.bearing.turn_left()

    def advance(self):
        if self.bearing == NORTH:
            self.y += 1
        elif self.bearing == SOUTH:
            self.y -= 1
        elif self.bearing == EAST:
            self.x += 1
        elif self.bearing == WEST:
            self.x -= 1
        else:
            raise ValueError

    def simulate(self, route):
        for action in route:
            if action == "L":
                self.turn_left()
            elif action == "R":
                self.turn_right()
            elif action == "A":
                self.advance()
            else:
                raise ValueError
