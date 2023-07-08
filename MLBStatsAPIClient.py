import requests
import pandas as pd
import sqlite3

class MLBStatsAPIClient:
    
    def __init__(self):
        base_url = "https://statsapi.mlb.com/api"
        pass
    
    #get game data
    def get_game(self, game_pk, timecode = None, hydrate = None, fields = None):
        request_url = f"{self.base_url}/v1.1/game/{game_pk}/feed/live"
    
        query_params = {}
    
        if timecode:
            query_params["timecode"] = timecode
            
        if hydrate:
            valid_hydrations = [h for h in hydrate if h in ["credits", "alignment", "flags", "officials", "preState"]]
        
            query_params["hydrate"] = ",".join(valid_hydrations)
        
        if fields:
            query_params["fields"] = ",".join(fields)
        
        response = requests.request(method="GET", url=request_url, params=query_params)
        
        #print(response.request.url)
    
        return pd.DataFrame(response.json())
    
    #get the list of team games by season
    def get_team_schedule_by_season(self, sport_id = None, season = None, game_type = None):
        request_url = f"{self.base_url}/v1/schedule/"
        
        query_params = {}
            
        if sport_id:
            query_params["sportId"] = sport_id
            
        if season:
            query_params["season"] = season
            
        if game_type:
            query_params["gameType"] = game_type
        
        response = requests.request(method="GET", url=request_url, params=query_params)
        
        #print(response.request.url)
    
        return pd.DataFrame(response.json())
    
    #get the list of teams by season
    def get_team_by_season(self, season = None, sport_id = None):
        request_url = f"{self.base_url}/v1/teams/"
        
        query_params = {}
        
        if season:
            query_params["season"] = season
            
        if sport_id:
            query_params["sportId"] = sport_id
        
        response = requests.request(method="GET", url=request_url, params=query_params)
        
        #print(response.request.url)
    
        return pd.DataFrame(response.json())
    
    #get list of players by season
    def get_player_by_season(self, sport_id, season = None, game_type = None):
        request_url = f"{self.base_url}/v1/sports/{sport_id}/players"
        
        query_params = {}
        
        if season:
            query_params["season"] = season
            
        if game_type:
            valid_game_type = [g for g in game_type if g in ["S","R","F","D","L","W","C","N","P","A","I","E"]]
            
            query_params["gameType"] = valid_game_type
            
        response = requests.request(method="GET", url=request_url, params=query_params)
        
        #print(response.request.url)
    
        return pd.DataFrame(response.json())
    
    #get player data
    def get_player(self, person_id, app_context = None, hydrate = None, fields = None):
        request_url = f"{self.base_url}/v1/people"
        
        query_params = {}
    
        if person_id:
            query_params["personIds"] = person_id
            
        if app_context:
            query_params["appContext"] = app_context
            
        if hydrate:
            #valid_hydrations = [h for h in hydrate if h in ["credits", "alignment", "flags", "officials", "preState"]]
        
            query_params["hydrate"] = ",".join(hydrate)
        
        if fields:
            query_params["fields"] = ",".join(fields)
        
        response = requests.request(method="GET", url=request_url, params=query_params)
        
        #print(response.request.url)
    
        return pd.DataFrame(response.json())