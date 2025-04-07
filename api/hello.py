#!/usr/bin/env python
from fastapi.routing import APIRouter
router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "FeiZhao World 2025！"}
