from pydantic import BaseModel
from typing import List

class TierInfo(BaseModel):
    queue : str = ''
    tier: str = 'unranked'
    division: str = ''
    lp: int = 0
    summonerName:str = ''

class TierListInfo(BaseModel):
    total_tier_list: List[TierInfo] = []
