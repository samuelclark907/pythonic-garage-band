class Musician:
    members = []

    def __init__(self, name, inst="flute"):
        self.name = name
        self.inst = inst
        self.solo = f"crazy {inst} solo"
        # self.__class__.members.append(self)

    
    def get_instrument(self):
        return self.inst

    def play_solo(self):
        return self.solo

    def __str__(self):
        return f'My name is {self.name} and I play {self.inst}'

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

   


class Band:
    instances = []
    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.instances.append(self.name)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        return [member.solo for member in self.members]


    @classmethod
    def to_list(cls):
        return cls.instances
    

class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.inst = 'guitar'
        self.solo = 'face melting guitar solo'



class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.inst = 'bass'
        self.solo = 'bom bom buh bom'




class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.inst = 'drums'
        self.solo = 'rattle boom crash'




if __name__ == "__main__":
    bands = []
    chicken = Band("lob")
    cow = Band('doll')
    bands.append(chicken)
    bands.append(cow)
    print(bands)