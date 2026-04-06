# ltb-fingerboard-designer

Fingerboard geometry: scale length, compound radius, fret positions, nut slots, fret leveling, wire selection, and nut compensation. Optional fret-slot CAM modules are included for library use.

**Source of truth:** [luthiers-toolbox](https://github.com/HanzoRazer/luthiers-toolbox) — populated via **Staged Copy Publish** (see `SPRINTS.md` there).

## Layout

```
src/ltb_fingerboard/
  calculators/          # fret_slots_*, fret_leveling, fret_wire, nut_slot, nut_compensation, temperaments
  instrument_geometry/  # models, neck/*, body/fretboard_geometry
  core/safety.py
  rmos/context.py       # slim RmosContext (from_model_id not bundled)
  data_registry/        # minimal Registry stub for CAM defaults
  schemas/cam_fret_slots.py
  api/fretwork_router.py
  main.py
frontend/src/components/  # Vue components copied from main client
```

## API

```bash
pip install -e .
uvicorn ltb_fingerboard.main:app --reload --host 0.0.0.0 --port 8000
```

- `GET /health`
- `GET /docs`
- Routes under `/api/instrument/` — nut slots, fret leveling, fret wire, nut compensation (same paths as monolith `fretwork_router`).

## Extra modules (not mounted as HTTP in this repo)

`fret_slots_cam`, `fret_slots_export`, `fret_slots_fan_cam` are included for import by tools or a future router; they depend on `RmosContext.from_dict()` and the local Registry stub.

## License

See `LICENSE`.
