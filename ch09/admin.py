from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, age, location, nick, privileges):
        super().__init__(first_name, last_name, age, location, nick)
        self.privileges = Privileges(privileges)
