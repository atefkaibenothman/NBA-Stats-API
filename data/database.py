from data.player import Player

class Database:
    # initializes an empty dictionary to start
    def __init__(self):
        self.db = dict()

    # returns the number of players in the database
    def __len__(self):
        return len(self.db)

    def __iter__(self):
        return self.db.__iter__()

    # prints player info and stats (id -> full_name)
    def list_all_players(self):
        for player_id,_player in self.db.items():
            # FINISH THIS
            _player.get_player_stats()


    # adds a player to the database if they haven't been added before
    def add_player(self, player_id, full_name, first_name, last_name, is_active):
        if player_id not in self.db:
            self.db[player_id] = Player(player_id, full_name, first_name, last_name, is_active)
        else:
            print(f"{player_id} is already in the database!")

    # adds a game log to the Player class
    def add_game_log(self, player_id, player_game_log):
        self.db[player_id].add_game_log_entry(player_game_log)