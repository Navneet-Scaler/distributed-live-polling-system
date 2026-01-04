from pydantic import BaseModel
from typing import Dict


class VoteRequest(BaseModel):
    option_id: str


class PollResults(BaseModel):
    poll_id: str
    results: Dict[str, int]
