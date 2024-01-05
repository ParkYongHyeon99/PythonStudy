import requests
from model.test1 import TierInfo, TierListInfo


def get_tier(queue, tier, division, lp) -> TierInfo:
    return TierInfo(
        queue=queue,
        tier=tier,
        division=division,
        lp=lp
    )


def test(riot_id: str,
         tag: str
         ) -> TierListInfo:
    api_key = 'RGAPI-798eb514-99d5-4a07-a165-d21c43381dc0'
    url1 = f'https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{riot_id}/{tag}?api_key={api_key}'
    res = requests.get(url1).json()
    puuid = res['puuid']

    url2 = f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}?api_key={api_key}'
    res2 = requests.get(url2).json()
    summoner_id = res2['id']

    url3 = f'https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}?api_key={api_key}'
    res3 = requests.get(url3).json()

    tier_list = []
    for league in res3:
        if league['queueType'] == 'RANKED_SOLO_5x5':
            queue = league['queueType']
            solo_rank_tier = league['tier']
            solo_rank_division = league['rank']
            solo_rank_lp = league['leaguePoints']
            tier = get_tier(queue, solo_rank_tier, solo_rank_division, solo_rank_lp)
            tier_list.append(tier)
        elif league['queueType'] == 'RANKED_FLEX_SR':
            queue = league['queueType']
            flex_rank_tier = league['tier']
            flex_rank_division = league['rank']
            flex_rank_lp = league['leaguePoints']
            tier = get_tier(queue, flex_rank_tier, flex_rank_division, flex_rank_lp)
            tier_list.append(tier)
    return TierListInfo(
        total_tier_list=tier_list
    )