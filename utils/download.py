import requests

from utils.response import Response

from nba_api.stats.static import players
from nba_api.stats.endpoints import PlayerGameLog

def download_all_players(database=None):
    """
    download all player basic info
    """
    # call nba_api and get all the players
    all_players = players.get_players()

    # initialize response with the specified database
    r = Response(all_players, database=database)

    # extract the response for only active players
    r.extract_active_players()


def download_player_game_log(player_id, SEASON, SEASON_TYPE, database=None):
    """
    download player game log
    src: https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/playergamelog.md
    """
    # call nba_api and get player game info
    pgl = PlayerGameLog(player_id).get_normalized_dict()

    # initialize response with the specified database
    r = Response(pgl, database=database)

    # extract the response for player game log
    r.extract_player_game_log(player_id)