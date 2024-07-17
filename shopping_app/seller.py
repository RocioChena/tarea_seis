from user import User
from ownable import Ownable
class Seller(User, Ownable):
    def init(self, name):
        super().init(name)