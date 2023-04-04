from fastapi import APIRouter

from src.assistance.schemas import AssistanceCreate, AssistanceList, AssistanceDetail, AssistanceUpdate

router = APIRouter()


@router.post("/assistance")
async def create_assistance(body: AssistanceCreate):
    pass


@router.get("/assistance", response_model=AssistanceList)
async def assistance_list():
    pass


@router.get("/assistance/{id}", response_model=AssistanceDetail)
async def assistance_detail(id: int):
    pass


@router.patch("/assistance/{id}", response_model=AssistanceUpdate)
async def assistance_update(id: int, body: AssistanceUpdate):
    pass


@router.delete("/assistance/{id}")
async def assistance_delete(id: int):
    pass
