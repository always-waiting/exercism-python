"""
- Earth: orbital period 365.25 Earth days, or 31557600 seconds
- Mercury: orbital period 0.2408467 Earth years
- Venus: orbital period 0.61519726 Earth years
- Mars: orbital period 1.8808158 Earth years
- Jupiter: orbital period 11.862615 Earth years
- Saturn: orbital period 29.447498 Earth years
- Uranus: orbital period 84.016846 Earth years
- Neptune: orbital period 164.79132 Earth years
"""
class SpaceAge(object):
    d2h = 24
    h2s = 3600
    y2d = 365.25
    y2s = y2d*d2h*h2s
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth = self.on_earth()
    def on_earth(self):
        if hasattr(self, "earth"):
            return self.earth
        else:
            return float("%.2f"% (self.seconds/SpaceAge.y2s))

    def on_mercury(self):
        return float("%.2f"% (self.earth/0.2408467))

    def on_venus(self):
        return float("%.2f"% (self.earth/0.61519726))

    def on_mars(self):
        return float("%.2f"% (self.earth/1.8808158))

    def on_jupiter(self):
        return float("%.2f"% (self.earth/11.862615))

    def on_saturn(self):
        return float("%.2f"% (self.earth/29.447498))

    def on_uranus(self):
        return float("%.2f"% (self.earth/84.016846))

    def on_neptune(self):
        return float("%.2f"% (self.earth/164.79132))
