import requests
import random
from model.test1 import TierInfo, TierListInfo

def get_tier(queue, summonerName, tier, division, lp) -> TierInfo:
    return TierInfo(
        queue=queue,
        summonerName=summonerName,
        tier=tier,
        division=division,
        lp=lp
    )

def test(tier: str,
         division: str
         ) -> 'TierListInfo':
    api_key = 'RGAPI-798eb514-99d5-4a07-a165-d21c43381dc0'
    url1 = f'https://kr.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/{tier}/{division}?api_key={api_key}'
    res = requests.get(url1).json()
    r_res = random.choices(res, k = 5)

    tier_list = []
    for league in r_res:
        if league['queueType'] == 'RANKED_SOLO_5x5':
            queue = league['queueType']
            summonerName = league['summonerName']
            solo_rank_tier = league['tier']
            solo_rank_division = league['rank']
            solo_rank_lp = league['leaguePoints']
            tier = get_tier(queue, summonerName, solo_rank_tier, solo_rank_division, solo_rank_lp)
            tier_list.append(tier)
        elif league['queueType'] == 'RANKED_FLEX_SR':
            queue = league['queueType']
            summonerName = league['summonerName']
            flex_rank_tier = league['tier']
            flex_rank_division = league['rank']
            flex_rank_lp = league['leaguePoints']
            tier = get_tier(queue, summonerName, flex_rank_tier, flex_rank_division, flex_rank_lp)
            tier_list.append(tier)
    return TierListInfo(
        total_tier_list=tier_list
    )







