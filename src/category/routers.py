from fastapi import APIRouter

from src.category.schemas import CategoryCreate, CategoryList, CategoryUpdate

router = APIRouter()


@router.post("/category", response_model=CategoryCreate)
async def create_category():
    pass


@router.get("/categories", response_model=CategoryList)
async def category_list():
    pass


@router.patch("/category/{id}", response_model=CategoryUpdate)
async def update_category(id: int, body: CategoryUpdate):
    pass


@router.delete("/category/{id}")
async def delete_category(id: int):
    pass
