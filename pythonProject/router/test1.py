from code1.test2 import test
from model.test1 import TierListInfo
from fastapi import APIRouter

router = APIRouter(prefix= '/summoner')

@router.get(
    path='/tier',
    response_model = TierListInfo
)
def summoner_tier(
        tier:str,
        division:str
) -> TierListInfo:
    return test(tier=tier, division = division)