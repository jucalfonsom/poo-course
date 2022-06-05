from account import Account

class User(Account):
    id = int
    email = str
    password = str


    def __init__(self, name: str, document: str, id: str, email: str, password: str) -> None:
        super().__init__(name, document)
        self.id = id
        self.email = email
        self.password = password