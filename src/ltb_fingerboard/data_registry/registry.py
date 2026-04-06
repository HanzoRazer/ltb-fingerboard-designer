"""Minimal Registry for fret CAM feedrate lookup (standalone)."""

from __future__ import annotations

from typing import Any, Dict, Optional


class Registry:
    """Subset of the Production Shop Registry — enough for fret CAM defaults."""

    def __init__(self, edition: str = "express", user_id: Optional[str] = None) -> None:
        self.edition = edition
        self.user_id = user_id

    def get_wood_species(self) -> Dict[str, Any]:
        return {
            "species": {
                "maple_hard": {"density_kg_m3": 705.0},
            }
        }


def get_registry(edition: str = "express", user_id: Optional[str] = None) -> Registry:
    return Registry(edition=edition, user_id=user_id)
