class Band:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"


class Musician:
    pass


class Guitarist:
    def __init__(self, name='Random'):
        self.name = name
        self.inst = 'guitar'

    def __str__(self):
        return f'My name is {self.name} and I play {self.inst}'

    # def __repr__(self):

   


class Bassist:
    pass

class Drummer:
    pass
