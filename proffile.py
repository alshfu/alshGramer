class User:

    def __init__(self):
        self.user_password = ""
        self.user_name = ""

    def set_user_name(self, user_name):
        self.user_name = user_name

    def set_user_password(self, password):
        self.user_password = password

    def get_user_name(self):
        return self.user_name

    def get_user_password(self):
        return self.user_password


class Target:
    target_list: list

    def get_target_list(self):
        target_list: list = ['ismailmustabirov']
        return target_list

    def __init__(self):
        self.target_list = self.get_target_list()
