# Holds all Player info
class Player:
    def __init__(self, id, full_name, first_name, last_name, is_active):
        self.id = id
        self.full_name = full_name
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = is_active
        self.game_log = dict()

    def get_id(self):
        return self.id

    def get_full_name(self):
        return self.full_name

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_is_active(self):
        return is_active

    def add_game_log_entry(self):
        pass