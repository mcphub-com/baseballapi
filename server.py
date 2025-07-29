import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/fluis.lacasse/api/baseballapi'

mcp = FastMCP('baseballapi')

@mcp.tool()
def search(term: Annotated[str, Field(description='The search term to use for finding baseball-related entities.')]) -> dict: 
    '''Search for baseball-related entities using the provided search term, and filter the results to show only baseball-related entities.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/search/mlb'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'term': term,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def match_player_statistics(id: Annotated[Union[int, float], Field(description='The ID of the baseball match for which you want to get the player statistics. Default: 9864379 Minimum: -9223372036854776000 Maximum: 9223372036854776000')],
                            playerId: Annotated[Union[int, float], Field(description='The player id. Default: 977489')]) -> dict: 
    '''Get the statistics for a specific baseball player in the match by providing its ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/match/9864379/player/977489/statistics'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'playerId': playerId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def match_lineups(id: Annotated[Union[int, float], Field(description='The ID of the baseball match for which you want to get the lineups. Default: 9864379 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the lineups for a specific baseball match by providing its ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/match/9864379/lineups'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def match_statistics(id: Annotated[Union[int, float], Field(description='The ID of the baseball match for which you want to get the statistics. Default: 9864379 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the statistics for a specific baseball match by providing its ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/match/9864379/statistics'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def match_highlights(id: Annotated[Union[int, float], Field(description='The ID of the match for which you want to get highlights. Default: 9864379 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the highlights of a specific baseball match using the match ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/match/9864379/highlights'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def match_schedules(day: Annotated[Union[int, float], Field(description='The day of the month for which you want to retrieve the match schedules (1-31). Default: 1 Minimum: -9223372036854776000 Maximum: 9223372036854776000')],
                    month: Annotated[Union[int, float], Field(description='The month for which you want to retrieve the match schedules (1-12). Default: 8 Minimum: -9223372036854776000 Maximum: 9223372036854776000')],
                    year: Annotated[Union[int, float], Field(description='The year for which you want to retrieve the match schedules (e.g., 2022). Default: 2022 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''This operation returns the baseball match schedules for the given date, including match timings, teams, and other relevant information.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/matches/1/8/2022'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'day': day,
        'month': month,
        'year': year,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def match_details(id: Annotated[Union[int, float], Field(description='The ID of the match for which you want to get the details. Default: 9864379 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get detailed information for a specific baseball match by providing the match ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/match/9864379'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def live_matches() -> dict: 
    '''Get live baseball matches that are currently taking place.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/matches/live'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def match_odds(id: Annotated[Union[int, float], Field(description='The ID of the match for which you want to get the odds. Default: 9864379 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the odds for a specific baseball match using the match ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/match/9864379/odds'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def match_h2_hduel(id: Annotated[Union[int, float], Field(description='The ID of the match for which you want to get the head-to-head duel. Default: 9864379 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the head-to-head duel for a specific baseball match using the match ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/match/9864379/duel'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def match_votes(id: Annotated[Union[int, float], Field(description='The ID of the match for which you want to get the votes. Default: 9864379 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the votes for a specific baseball match using the match ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/match/9864379/votes'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def head_to_head_matches(customId: Annotated[str, Field(description='The custom ID of the match for which you want to get the head-to-head matches.')]) -> dict: 
    '''Get head-to-head match data for a specific baseball match using its custom ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/match/ExbsIxb/h2h'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'customId': customId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def pre_match_form(id: Annotated[Union[int, float], Field(description='The ID of the match for which you want to get the pre-match form. Default: 9864379 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the pre-match form for a specific baseball match using the match ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/match/9864379/form'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def player_near_matches(id: Annotated[Union[int, float], Field(description='The player ID for which you want to retrieve the near matches. Default: 977489 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the near matches for a specific baseball player using the player ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/player/977489/matches/near'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def player_regular_season_statistics(id: Annotated[Union[int, float], Field(description='The player ID for which you want to retrieve the statistics. Default: 977489 Minimum: -9223372036854776000 Maximum: 9223372036854776000')],
                                     tournamentId: Annotated[Union[int, float], Field(description="The unique tournament ID for which you want to retrieve the player's statistics. Default: 11205 Minimum: -9223372036854776000 Maximum: 9223372036854776000")],
                                     seasonId: Annotated[Union[int, float], Field(description="The season ID for which you want to retrieve the player's statistics. Default: 29168 Minimum: -9223372036854776000 Maximum: 9223372036854776000")]) -> dict: 
    '''Get the regular season statistics for a specific baseball player using the player ID, tournament ID, and season ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/player/977489/tournament/11205/season/29168/statistics/regularSeason'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'tournamentId': tournamentId,
        'seasonId': seasonId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def player_statistics_seasons(id: Annotated[Union[int, float], Field(description='The player ID for which you want to retrieve the statistics seasons. Default: 977489 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the statistics seasons for a specific baseball player using the player ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/player/977489/statistics/seasons'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def player_last_matches(id: Annotated[Union[int, float], Field(description='The ID of the player for which you want to retrieve the last matches. Default: 1195558 Minimum: -9223372036854776000 Maximum: 9223372036854776000')],
                        page: Annotated[Union[int, float], Field(description='Zero-based page number. Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the last matches played by a specific Baseball player by providing the player ID and page number.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/player/1195558/matches/previous/%7Bpage%7D'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def player_image(id: Annotated[Union[int, float], Field(description='The player ID for which you want to retrieve the image. Default: 977489 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the image for a specific baseball player using the player ID. Generates a PNG image.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/player/977489/image'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def player_details(id: Annotated[Union[int, float], Field(description='The player ID for which you want to retrieve the details. Default: 977489 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the details for a specific baseball player using the player ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/player/977489'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def team_standings_seasons(id: Annotated[Union[int, float], Field(description='The ID of the team for which you want to retrieve the team standings for different seasons. Default: 3633 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the team standings for different seasons for a given team by providing its ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/team/3633/standings/seasons'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def team_tournaments(id: Annotated[Union[int, float], Field(description='The ID of the team for which you want to retrieve the tournaments. Default: 3633 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the tournaments in which a specific baseball team participates.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/team/3633/tournaments'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def team_logo_image(id: Annotated[Union[int, float], Field(description='The team ID for which you want to retrieve the logo image. Default: 3633 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the logo image for a specific baseball team using the team ID. Generates a PNG image.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/team/3633/image'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def team_next_matches(id: Annotated[Union[int, float], Field(description='The ID of the team for which you want to retrieve upcoming matches. Default: 3633 Minimum: -9223372036854776000 Maximum: 9223372036854776000')],
                      page: Annotated[Union[int, float], Field(description='The page number (zero-based) of the results you want to retrieve. Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get upcoming baseball matches for a specific team.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/team/3633/matches/next/%7Bpage%7D'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def team_details(id: Annotated[Union[int, float], Field(description='The team ID for which you want to retrieve the details. Default: 3633 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the details for a specific baseball team using the team ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/team/3633'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def team_near_matches(id: Annotated[Union[int, float], Field(description='The team ID for which you want to retrieve the near matches. Default: 3633 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the near matches for a specific baseball team using the team ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/team/3633/matches/near'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def team_last_matches(id: Annotated[Union[int, float], Field(description='The ID of the baseball team for which you want to retrieve the last matches. Default: 3633 Minimum: -9223372036854776000 Maximum: 9223372036854776000')],
                      page: Annotated[Union[int, float], Field(description='The zero-based page number of the results you want to retrieve. Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the last matches for a specific baseball team by providing its ID and page number.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/team/3633/matches/previous/%7Bpage%7D'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def team_media(id: Annotated[Union[int, float], Field(description='The team ID for which you want to retrieve the media. Default: 3633 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the media for a specific baseball team using the team ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/team/3633/media'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def team_players(id: Annotated[Union[int, float], Field(description='The team ID for which you want to retrieve the players. Default: 3633 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the players for a specific baseball team using the team ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/team/3633/players'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def league_away_standings(tournamentId: Annotated[Union[int, float], Field(description='The unique tournament ID for which you want to retrieve the away standings. Default: 19442 Minimum: -9223372036854776000 Maximum: 9223372036854776000')],
                          seasonId: Annotated[Union[int, float], Field(description='The ID of the season for which you want to retrieve the away standings. Default: 49349 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the away standings of a specific baseball league for a specific season.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/tournament/19442/season/49349/standings/away'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tournamentId': tournamentId,
        'seasonId': seasonId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def league_details(tournamentId: Annotated[Union[int, float], Field(description="The unique tournament ID for which you want to retrieve the league's details. Default: 11205 Minimum: -9223372036854776000 Maximum: 9223372036854776000")]) -> dict: 
    '''Get the details of a specific baseball league using the unique tournament ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/tournament/11205'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tournamentId': tournamentId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def league_home_standings(tournamentId: Annotated[Union[int, float], Field(description='The unique tournament ID for which you want to retrieve the home standings. Default: 19442 Minimum: -9223372036854776000 Maximum: 9223372036854776000')],
                          seasonId: Annotated[Union[int, float], Field(description='The ID of the season for which you want to retrieve the home standings. Default: 49349 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the home standings of a specific baseball league for a specific season.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/tournament/19442/season/49349/standings/home'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tournamentId': tournamentId,
        'seasonId': seasonId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def league_total_standings(tournamentId: Annotated[Union[int, float], Field(description='The unique tournament ID for which you want to retrieve the total standings. Default: 11205 Minimum: -9223372036854776000 Maximum: 9223372036854776000')],
                           seasonId: Annotated[Union[int, float], Field(description='The ID of the season for which you want to retrieve the total standings. Default: 29168 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the total standings of a specific baseball league for a specific season.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/tournament/11205/season/29168/standings/total'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tournamentId': tournamentId,
        'seasonId': seasonId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def league_next_matches(tournamentId: Annotated[Union[int, float], Field(description="The unique tournament ID for which you want to retrieve the league's next matches. Default: 11205 Minimum: -9223372036854776000 Maximum: 9223372036854776000")],
                        seasonId: Annotated[Union[int, float], Field(description="The season ID for which you want to retrieve the league's next matches. Default: 39143 Minimum: -9223372036854776000 Maximum: 9223372036854776000")],
                        page: Annotated[Union[int, float], Field(description='Zero-based page. Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the next matches for a specific baseball league using the tournament ID, season ID, and page.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/tournament/11205/season/39143/matches/next/%7Bpage%7D'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tournamentId': tournamentId,
        'seasonId': seasonId,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def league_media(tournamentId: Annotated[Union[int, float], Field(description='The unique tournament ID for which you want to retrieve the league media. Default: 11205 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the media for a specific baseball league using the unique tournament ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/tournament/11205/media'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tournamentId': tournamentId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def league_total_team_events(tournamentId: Annotated[Union[int, float], Field(description='The unique tournament ID for which you want to retrieve the total team events. Default: 19442 Minimum: -9223372036854776000 Maximum: 9223372036854776000')],
                             seasonId: Annotated[Union[int, float], Field(description='The ID of the season for which you want to retrieve the total team events. Default: 49349 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''This endpoint retrieves the last 5 matches for a specific league in a given season for both home and away events.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/tournament/19442/season/49349/team-events/total'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tournamentId': tournamentId,
        'seasonId': seasonId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def league_cup_trees(tournamentId: Annotated[Union[int, float], Field(description='The unique tournament ID for which you want to retrieve the league cup trees. Default: 11205 Minimum: -9223372036854776000 Maximum: 9223372036854776000')],
                     seasonId: Annotated[Union[int, float], Field(description='The season ID for which you want to retrieve the league cup trees. Default: 29168 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the cup trees for a specific baseball league using the tournament ID and season ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/tournament/11205/season/29168/cuptrees'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tournamentId': tournamentId,
        'seasonId': seasonId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def category_tournaments(id: Annotated[Union[int, float], Field(description='The category ID for which you want to retrieve all leagues. Default: 1374 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get a list of all leagues from a specific baseball category using the category ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/tournament/all/category/1374'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def league_away_team_events(tournamentId: Annotated[Union[int, float], Field(description='The unique tournament ID for which you want to retrieve the away team events. Default: 19442 Minimum: -9223372036854776000 Maximum: 9223372036854776000')],
                            seasonId: Annotated[Union[int, float], Field(description='The ID of the season for which you want to retrieve the away team events. Default: 49349 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''This endpoint retrieves the last 5 matches for a specific league in a given season for away events.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/tournament/19442/season/49349/team-events/away'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tournamentId': tournamentId,
        'seasonId': seasonId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def league_seasons(tournamentId: Annotated[Union[int, float], Field(description="The unique tournament ID for which you want to retrieve the league's seasons. Default: 11205 Minimum: -9223372036854776000 Maximum: 9223372036854776000")]) -> dict: 
    '''Get the seasons for a specific baseball league using the unique tournament ID.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/tournament/11205/seasons'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tournamentId': tournamentId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def category_schedules(id: Annotated[Union[int, float], Field(description='The category ID for which you want to retrieve the schedules. Default: 1374 Minimum: -9223372036854776000 Maximum: 9223372036854776000')],
                       day: Annotated[Union[int, float], Field(description='The day for which you want to retrieve the schedules. Default: 1 Minimum: -9223372036854776000 Maximum: 9223372036854776000')],
                       month: Annotated[Union[int, float], Field(description='The month for which you want to retrieve the schedules. Default: 8 Minimum: -9223372036854776000 Maximum: 9223372036854776000')],
                       year: Annotated[Union[int, float], Field(description='The year for which you want to retrieve the schedules. Default: 2022 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the baseball match schedules for a specific day and category using the category ID, day, month, and year.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/category/1374/events/1/8/2022'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'day': day,
        'month': month,
        'year': year,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def league_logo_image(tournamentId: Annotated[Union[int, float], Field(description='The unique tournament ID for which you want to retrieve the league logo image. Default: 11205 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the logo image for a specific baseball league using the unique tournament ID. Generates a PNG image.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/tournament/11205/image'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tournamentId': tournamentId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def league_last_matches(tournamentId: Annotated[Union[int, float], Field(description='The unique tournament ID for which you want to retrieve the last matches. Default: 11205 Minimum: -9223372036854776000 Maximum: 9223372036854776000')],
                        seasonId: Annotated[Union[int, float], Field(description='The season ID for which you want to retrieve the last matches. Default: 39143 Minimum: -9223372036854776000 Maximum: 9223372036854776000')],
                        page: Annotated[Union[int, float], Field(description='The 0-based page number for which you want to retrieve the last matches. Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Get the last matches for a league by providing the unique tournament ID, season ID, and the page number (0-based).'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/tournament/11205/season/39143/matches/last/%7Bpage%7D'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tournamentId': tournamentId,
        'seasonId': seasonId,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def league_home_team_events(tournamentId: Annotated[Union[int, float], Field(description='The unique tournament ID for which you want to retrieve the home team events. Default: 19442 Minimum: -9223372036854776000 Maximum: 9223372036854776000')],
                            seasonId: Annotated[Union[int, float], Field(description='The ID of the season for which you want to retrieve the home team events. Default: 49349 Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''This endpoint retrieves the last 5 matches for a specific league in a given season for home events.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/tournament/19442/season/49349/team-events/home'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tournamentId': tournamentId,
        'seasonId': seasonId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def categories() -> dict: 
    '''Get a list of all baseball categories.'''
    url = 'https://baseballapi.p.rapidapi.com/api/baseball/tournament/categories'
    headers = {'x-rapidapi-host': 'baseballapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
