

class Point():
    
    def __init__(self, name, long, lat):

        if not (-180 <= long <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        
        if not (-180 <= lat <= 180):
            raise ValueError("Latitude must be between -180 and 180")
    
        if isinstance(name, str) is False:
            raise TypeError("name must be a string")
        
        self.name = name
        self.long = long
        self.lat = lat

    def get_location(self):
        return (self.long, self.lat)

