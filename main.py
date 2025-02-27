from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from budget_service.main import budget_router
from goal_service.main import goals_router
from common.config import ORIGINS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(budget_router, prefix="/api/v1")
app.include_router(goals_router, prefix="/api/v1")
