from data.database import Database

# goes through the response from nba_api and extracts the relevant info
class Response:
    def __init__(self, resp, database=None):
        self.resp = resp
        self.db = database

    # extract only active player info
    def extract_active_players(self):
        for player in self.resp:
            if (player["is_active"]):
                id         = player["id"]
                full_name  = player["full_name"]
                first_name = player["first_name"]
                last_name  = player["last_name"]
                is_active  = player["is_active"]
                
                if (self.db != None):
                    self.db.add_player(id, full_name, first_name, last_name, is_active)
                else:
                    print("database not specified... cannot add player!")