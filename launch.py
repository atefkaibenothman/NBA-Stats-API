from data.database import Database
from utils.download import (
    download_all_players,
    download_player_game_log,
    download_common_player_info,
)

# GLOBALS
SEASON = "2019-2020"
SEASON_TYPE = "Regular Season"
LEAGUE_ID = "00"


# starts the program
def start():
    # initialize a database
    db = Database()
    # download all player basic info
    download_all_players(database=db)
    return db


# iterates through all players and updates the databases w/ updated statistics
def download_game_log(db, COUNT=25):
    i = 1
    for player_id in db:
        download_player_game_log(player_id, SEASON, SEASON_TYPE, database=db)
        i += 1
        if i >= COUNT:
            return


# iterates through all players and updates the database w/ updated info (team_id, postition, etc.)
def get_player_common_info(db):
    for player_id in db:
        download_common_player_info(player_id, database=db)


if __name__ == "__main__":
    db = start()
    get_player_common_info(db)

    # download_game_log(db, COUNT=1)
    # db.list_all_players()

    db.insert_player_data()
    db.close_connection()
