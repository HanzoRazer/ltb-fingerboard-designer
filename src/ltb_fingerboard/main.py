"""FastAPI entrypoint for LTB Fingerboard Designer."""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ltb_fingerboard.api.fretwork_router import router as fretwork_router

app = FastAPI(
    title="LTB Fingerboard Designer",
    description="Fret math, nut slots, leveling, wire selection, nut compensation — published from luthiers-toolbox.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(fretwork_router, prefix="/api/instrument")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "ltb-fingerboard-designer"}
