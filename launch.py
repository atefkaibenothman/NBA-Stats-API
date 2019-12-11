from data.database import Database
from utils.download import download_all_players, download_player_game_log

# GLOBALS
SEASON = "2019-2020"
SEASON_TYPE = "Regular Season"
LEAGUE_ID = "00"

def start():
    """
    starts the entire program
    """
    # initialize a database
    db = Database()

    # download all player basic info 
    download_all_players(database=db)

    return db

def download_game_log(db):
    """
    iterates through all players and updates the database w/ updated statistics
    """
    for player_id in db:
        download_player_game_log(player_id, SEASON, SEASON_TYPE)


if __name__ == "__main__":
    db = start()
    download_game_log(db)