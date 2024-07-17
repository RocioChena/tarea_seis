class Ownable:
    def __init__(self, owner=None):
        self.owner = owner

    def set_owner(self, owner):
        self.owner = owner
