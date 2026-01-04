from fastapi import APIRouter, HTTPException
from app.schemas.poll import VoteRequest, PollResults

from app.services.polling_service import PollingService

router = APIRouter()

polling_service = PollingService()


@router.post("/vote/{poll_id}")
async def vote(poll_id: str, payload: VoteRequest):
    try:
        await polling_service.vote(poll_id, payload.option_id)
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/results/{poll_id}", response_model=PollResults)
async def get_results(poll_id: str):
    try:
        results = await polling_service.get_results(poll_id)
        return PollResults(poll_id=poll_id, results=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
