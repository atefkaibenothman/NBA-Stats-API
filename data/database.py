from data.player import Player

# stores all data
class Database:
    # initializes an empty dictionary to start
    def __init__(self):
        self.db = dict()

    # returns the number of players in the database
    def __len__(self):
        return len(self.db)

    # prints player info (id -> full_name)
    def list_all_players(self):
        for k,v in self.db.items():
            print(f"{k:>12} : {v.full_name:>12}")

    # adds a player to the database if they haven't been added before
    def add_player(self, player_id, full_name, first_name, last_name, is_active):
        if player_id not in self.db:
            self.db[player_id] = Player(player_id, full_name, first_name, last_name, is_active)
        else:
            print(f"{player_id} is already in the database!")

