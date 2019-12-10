from data.database import Database
from utils.download import download_all_players

def start():
    # initialize a database
    db = Database()
    # download all player basic info 
    download_all_players(database=db)
    # lists all the players
    db.list_all_players()

if __name__ == "__main__":
    # starts the entire program
    start()