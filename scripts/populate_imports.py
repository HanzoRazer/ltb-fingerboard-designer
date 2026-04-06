"""One-off import rewriter for Staged Copy Publish (run from repo root)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "src" / "ltb_fingerboard"


def rewrite(text: str) -> str:
    # Monolith app package -> standalone
    text = re.sub(r"\bfrom app\.calculators\.", "from ltb_fingerboard.calculators.", text)
    text = re.sub(r"\bfrom app\.core\.safety import", "from ltb_fingerboard.core.safety import", text)
    text = re.sub(r"\bfrom app\.core\.", "from ltb_fingerboard.core.", text)
    text = re.sub(r"\bfrom app\.instrument_geometry\.", "from ltb_fingerboard.instrument_geometry.", text)
    text = re.sub(r"\bfrom app\.schemas\.", "from ltb_fingerboard.schemas.", text)
    text = re.sub(r"\bfrom app\.rmos\.", "from ltb_fingerboard.rmos.", text)
    # Parent-relative from calculators/
    text = re.sub(r"\bfrom \.\.instrument_geometry\.", "from ltb_fingerboard.instrument_geometry.", text)
    text = re.sub(r"\bfrom \.\.core\.", "from ltb_fingerboard.core.", text)
    text = re.sub(r"\bfrom \.\.rmos\.", "from ltb_fingerboard.rmos.", text)
    text = re.sub(r"\bfrom \.\.data_registry\b", "from ltb_fingerboard.data_registry", text)
    text = re.sub(r"\bfrom \.\.schemas\.", "from ltb_fingerboard.schemas.", text)
    return text


def main() -> None:
    for path in ROOT.rglob("*.py"):
        raw = path.read_text(encoding="utf-8")
        new = rewrite(raw)
        if new != raw:
            path.write_text(new, encoding="utf-8")
            print("updated", path.relative_to(ROOT.parent.parent))


if __name__ == "__main__":
    main()
