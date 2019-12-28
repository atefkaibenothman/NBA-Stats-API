import requests

from utils.response import Response

from nba_api.stats.static import players
from nba_api.stats.endpoints import PlayerGameLog, commonplayerinfo

# download all player basic info
# https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/static/players.md
def download_all_players(database=None):
    # call nba_api and get all the players
    all_players = players.get_players()

    # initialize response with the specified database
    r = Response(all_players, database=database)

    # extract the response for only active players
    r.extract_active_players()


# download player game log
# https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/playergamelog.md
def download_player_game_log(player_id, SEASON, SEASON_TYPE, database=None):
    # call nba_api and get player game info
    pgl = PlayerGameLog(player_id).get_normalized_dict()

    # initialize response with the specified database
    r = Response(pgl, database=database)

    # extract the response for player game log
    r.extract_player_game_log(player_id)


# download common player info
# https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/commonplayerinfo.md
def download_common_player_info(player_id, database=None):
    # call nba_api and get common player info
    cpi = commonplayerinfo.CommonPlayerInfo(player_id).get_normalized_dict()

    # initialize response with the specified database
    r = Response(cpi, database=database)

    # extract the response for player common info
    r.extract_player_common_info(player_id)
