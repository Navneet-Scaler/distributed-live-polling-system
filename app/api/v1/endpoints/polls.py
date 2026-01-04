from fastapi import APIRouter, HTTPException

from app.services.polling_service import PollingService
from app.api.schemas.poll import VoteRequest, PollResults

router = APIRouter()

polling_service = PollingService()


@router.post("/vote/{poll_id}")
async def vote(poll_id: str, request: VoteRequest):
    try:
        await polling_service.vote(poll_id, request.option_id)
        return {"status": "vote recorded"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/results/{poll_id}", response_model=PollResults)
async def get_results(poll_id: str):
    try:
        results = await polling_service.get_results(poll_id)
        return PollResults(
            poll_id=poll_id,
            results=results,
            served_via="in_memory"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
