# Trimmed from luthiers-toolbox — full preset loading (from_model_id) not bundled.
"""RMOS Context: manufacturing context for fret CAM (standalone subset)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from enum import Enum


class CutType(str, Enum):
    SAW = "saw"
    ROUTE = "route"
    DRILL = "drill"
    MILL = "mill"
    SAND = "sand"


class WoodSpecies(str, Enum):
    MAPLE = "maple"
    MAHOGANY = "mahogany"
    ROSEWOOD = "rosewood"
    EBONY = "ebony"
    SPRUCE = "spruce"
    CEDAR = "cedar"
    WALNUT = "walnut"
    ASH = "ash"
    ALDER = "alder"
    KOA = "koa"
    BASSWOOD = "basswood"
    UNKNOWN = "unknown"


@dataclass
class MaterialProfile:
    species: WoodSpecies = WoodSpecies.MAPLE
    thickness_mm: float = 25.4
    density_kg_m3: float = 705.0
    hardness_janka_n: Optional[float] = None
    moisture_content_pct: float = 8.0
    notes: str = ""


@dataclass
class SafetyConstraints:
    max_feed_rate_mm_min: float = 2000.0
    max_spindle_rpm: float = 24000.0
    max_plunge_rate_mm_min: float = 500.0
    min_tool_diameter_mm: float = 1.5
    max_tool_diameter_mm: float = 25.4
    max_depth_of_cut_mm: float = 3.0
    require_dust_collection: bool = True
    require_safety_stops: bool = True
    notes: str = ""


@dataclass
class CutOperation:
    operation_id: str
    cut_type: CutType
    tool_id: str
    feed_rate_mm_min: float
    spindle_rpm: float
    depth_mm: float
    description: str = ""
    gcode_file: Optional[str] = None
    estimated_time_seconds: Optional[float] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ToolpathData:
    source_file: str
    format: str
    path_count: int = 0
    total_length_mm: float = 0.0
    bounds_mm: List[float] = field(default_factory=lambda: [0.0, 0.0, 0.0, 0.0])
    geometry: Optional[Any] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class RmosContext:
    model_id: str
    model_spec: Dict[str, Any]
    toolpaths: Optional[ToolpathData] = None
    materials: Optional[MaterialProfile] = None
    cuts: Optional[List[CutOperation]] = None
    safety_constraints: Optional[SafetyConstraints] = None
    physics_inputs: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_model_id(cls, model_id: str) -> "RmosContext":
        raise NotImplementedError(
            "Preset model loading is not bundled in ltb-fingerboard-designer; "
            "use RmosContext.from_dict() or build RmosContext directly."
        )

    @classmethod
    def from_dict(cls, payload: Dict[str, Any]) -> "RmosContext":
        model_id = payload.get("model_id", "unknown")
        model_spec = payload.get("model_spec", {})
        materials_data = payload.get("materials")
        materials = MaterialProfile(**materials_data) if materials_data else None
        safety_data = payload.get("safety_constraints")
        safety = SafetyConstraints(**safety_data) if safety_data else None
        toolpaths_data = payload.get("toolpaths")
        toolpaths = ToolpathData(**toolpaths_data) if toolpaths_data else None
        cuts_data = payload.get("cuts")
        cuts = [CutOperation(**cut) for cut in cuts_data] if cuts_data else None
        return cls(
            model_id=model_id,
            model_spec=model_spec,
            toolpaths=toolpaths,
            materials=materials,
            cuts=cuts,
            safety_constraints=safety,
            physics_inputs=payload.get("physics_inputs", {}),
            metadata=payload.get("metadata", {}),
        )

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {
            "model_id": self.model_id,
            "model_spec": self.model_spec,
            "physics_inputs": self.physics_inputs,
            "metadata": self.metadata,
        }
        if self.toolpaths:
            result["toolpaths"] = {
                "source_file": self.toolpaths.source_file,
                "format": self.toolpaths.format,
                "path_count": self.toolpaths.path_count,
                "total_length_mm": self.toolpaths.total_length_mm,
                "bounds_mm": self.toolpaths.bounds_mm,
                "metadata": self.toolpaths.metadata,
            }
        if self.materials:
            result["materials"] = {
                "species": self.materials.species.value,
                "thickness_mm": self.materials.thickness_mm,
                "density_kg_m3": self.materials.density_kg_m3,
                "hardness_janka_n": self.materials.hardness_janka_n,
                "moisture_content_pct": self.materials.moisture_content_pct,
                "notes": self.materials.notes,
            }
        if self.cuts:
            result["cuts"] = [
                {
                    "operation_id": cut.operation_id,
                    "cut_type": cut.cut_type.value,
                    "tool_id": cut.tool_id,
                    "feed_rate_mm_min": cut.feed_rate_mm_min,
                    "spindle_rpm": cut.spindle_rpm,
                    "depth_mm": cut.depth_mm,
                    "description": cut.description,
                    "gcode_file": cut.gcode_file,
                    "estimated_time_seconds": cut.estimated_time_seconds,
                    "metadata": cut.metadata,
                }
                for cut in self.cuts
            ]
        if self.safety_constraints:
            result["safety_constraints"] = {
                "max_feed_rate_mm_min": self.safety_constraints.max_feed_rate_mm_min,
                "max_spindle_rpm": self.safety_constraints.max_spindle_rpm,
                "max_plunge_rate_mm_min": self.safety_constraints.max_plunge_rate_mm_min,
                "min_tool_diameter_mm": self.safety_constraints.min_tool_diameter_mm,
                "max_tool_diameter_mm": self.safety_constraints.max_tool_diameter_mm,
                "max_depth_of_cut_mm": self.safety_constraints.max_depth_of_cut_mm,
                "require_dust_collection": self.safety_constraints.require_dust_collection,
                "require_safety_stops": self.safety_constraints.require_safety_stops,
                "notes": self.safety_constraints.notes,
            }
        return result

    def validate(self) -> List[str]:
        errors: List[str] = []
        if not self.model_id:
            errors.append("model_id is required")
        if not self.model_spec:
            errors.append("model_spec is required")
        if self.materials:
            if self.materials.thickness_mm <= 0:
                errors.append(f"Invalid material thickness: {self.materials.thickness_mm}mm")
            if self.materials.density_kg_m3 <= 0:
                errors.append(f"Invalid material density: {self.materials.density_kg_m3} kg/m³")
        if self.safety_constraints:
            if self.safety_constraints.max_feed_rate_mm_min <= 0:
                errors.append(f"Invalid max feed rate: {self.safety_constraints.max_feed_rate_mm_min}")
            if self.safety_constraints.max_spindle_rpm <= 0:
                errors.append(f"Invalid max spindle RPM: {self.safety_constraints.max_spindle_rpm}")
        if self.cuts:
            for i, cut in enumerate(self.cuts):
                if cut.feed_rate_mm_min <= 0:
                    errors.append(f"Cut #{i} has invalid feed rate: {cut.feed_rate_mm_min}")
                if cut.spindle_rpm < 0:
                    errors.append(f"Cut #{i} has invalid spindle RPM: {cut.spindle_rpm}")
                if cut.depth_mm < 0:
                    errors.append(f"Cut #{i} has invalid depth: {cut.depth_mm}")
        return errors
