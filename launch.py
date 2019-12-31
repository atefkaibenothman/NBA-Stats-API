from data.database import Database
from utils.download import (
    download_all_players,
    download_player_game_log,
    download_common_player_info,
    download_all_teams,
)

# GLOBALS
SEASON = "2019-2020"
SEASON_TYPE = "Regular Season"
LEAGUE_ID = "00"


# handles the intialization of the database and the creation of necessary tables
def setup_database():
    # intialize empty database
    db = Database()

    # create 'Player' table
    db.create_player_table()

    # create 'Team' table
    db.create_team_table()

    return db


# retrieves the active players and inserts them into the database
def retrieve_active_players(db):
    # retrieve active players
    download_all_players(database=db)

    # retrieve common player info
    download_common_player_info(db)

    # insert player data into postgres database
    db.insert_player_data()


# retrieves the team info
def retrieve_teams(db):
    # retrieve teams
    download_all_teams(db)

    # insert team data in postgres database
    db.insert_team_data()


# retrieves the game stats for each player
def retrieve_player_game_logs(db, COUNT=10):
    download_player_game_log(player_id, SEASON, SEASON_TYPE, database=db, COUNT=COUNT)


if __name__ == "__main__":
    db = setup_database()
    # retrieve_active_players(db) already done
    # retrieve_teams(db) already done
    retrieve_player_game_logs(db, COUNT=1)
    db.close_connection()
