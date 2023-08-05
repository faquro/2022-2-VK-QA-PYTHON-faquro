from .models import User


class MySQLBuilder:

    def __init__(self, client):
        self.client = client
        self.User = User.__table__

    def get_users(self):
        users = self.client.session.query(self.User).all()
        return [item.username for item in users]


    def get_user_by_name(self, username):
        row = self.client.session.query(self.User).filter_by(username=username).first()
        return row


    def is_active(self, username):
        row = self.get_user_by_name(username)
        return row.active == 1

    def user_exists(self, username):
        self.client.session.commit()
        row = self.get_user_by_name(username)
        return row.username == username
