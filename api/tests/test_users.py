class Session:
    cont = 0
    users = []

    def save(self, user):
        Session.cont += 1
        user.id = Session.cont
        self.users.append(user)

    def get_all(self):
        return self.users

    def roll_back(self):
        pass

    def close(self):
        pass

class Connection:
    def create_session(self):
        return Session
    
    def close(self):
        pass

class User:
    def __init__(self, name, email):
        self.id = None
        self.name = name
        self.email = email


def test_salvar_usuario():
    conn = Connection()
    session = conn.create_session()
    user = User(name="User Teste", email="test@test.com")
    session.save(user)
    assert isinstance(user.id, int)
    session.roll_back()
    session.close()
    conn.close()


def test_list_users():
    conn = Connection()
    session = conn.create_session()
    users = [
        User(name="User Teste", email="test@test.com"), 
        User(name="User Teste2", email="test2@test.com")
        ]
    for user in users:
        session.save(user)
    assert users == session.get_all()
    session.roll_back()
    session.close()
    conn.close()
