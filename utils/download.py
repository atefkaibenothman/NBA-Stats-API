import requests

from utils.response import Response

from nba_api.stats.static import players

# download all player basic info
def download_all_players(database=None):
    # call nba_api and get all the players
    all_players = players.get_players()

    # initialize response with the specified database
    r = Response(all_players, database=database)
    
    # extract the response for only active players
    r.extract_active_players()
