from data.database import Database

# goes through the response from nba_api and extracts the relevant info
class Response:
    def __init__(self, resp, database=None):
        self.resp = resp
        self.db = database

    # extract only active player info
    def extract_active_players(self):
        print("extracting active player templates...")
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

    # extract game log for players
    def extract_player_game_log(self, player_id):
        print(f"extracting player game logs for {player_id}...")
        for game in self.resp["PlayerGameLog"]:
            game_id = game["Game_ID"]           # game ID
            season_id = game["SEASON_ID"]       # season ID
            player_id = game["Player_ID"]       # player ID
            game_date = game["GAME_DATE"]       # game date
            matchup = game["MATCHUP"]           # team vs. team
            win_lose = game["WL"]               # win/lose
            min_played = game["MIN"]            # minutes played
            fgm = game["FGM"]                   # field goals made
            fga = game["FGA"]                   # field goals attempted
            fg_pct = game["FG_PCT"]             # field goal percentage
            fg3m = game["FG3M"]                 # 3point field goals made
            fg3a = game["FG3A"]                 # 3point field goals attempted
            fg3_pct = game["FG3_PCT"]           # 3point field goal percentage
            ftm = game["FTM"]                   # free throws made
            fta = game["FTA"]                   # free throws attempted
            ft_pct = game["FT_PCT"]             # free throw percentage
            oreb = game["OREB"]                 # offensive rebounds
            dreb = game["DREB"]                 # defensive rebounds
            tot_reb = game["REB"]               # total rebounds
            ast = game["AST"]                   # assists
            stl = game["STL"]                   # steals
            blk = game["BLK"]                   # blocks
            tov = game["TOV"]                   # turnovers
            pf = game["PF"]                     # personal fouls
            pts = game["PTS"]                   # points
            plus_minus = game["PLUS_MINUS"]     # plus/minus