# ltb-fingerboard-designer

LTB Fingerboard Designer - Fingerboard radius, scale, and multiscale calculator

## Status

🚧 **Minimal Skeleton** - Features extracted from golden master as needed.

**Strategy:** Lean extraction (no template stubs)  
**Approach:** Clean slate → Extract specific features incrementally  
**Benefit:** Only includes code that's actually implemented

## Quick Start

### Server (FastAPI)

**Dependencies already installed!** Just activate and run:

```powershell
cd server
.\.venv\Scripts\Activate.ps1
copy .env.example .env
uvicorn app.main:app --reload
```

**If you need to reinstall:**

```powershell
cd server
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Client Setup

```powershell
cd client
npm create vite@latest . -- --template vue-ts
npm install
npm run dev
```

## Extracting Features

1. Identify feature in [Golden Master](https://github.com/HanzoRazer/luthiers-toolbox)
2. Copy specific files/components needed
3. Strip unnecessary features (downgrade to edition tier)
4. Test extraction
5. Commit with clear feature description

## Documentation

- [Product Segmentation Strategy](https://github.com/HanzoRazer/luthiers-toolbox/blob/main/docs/products/MASTER_SEGMENTATION_STRATEGY.md)
- [Setup Guide](https://github.com/HanzoRazer/luthiers-toolbox/blob/main/PRODUCT_REPO_SETUP.md)

## Related Repositories

- [Golden Master](https://github.com/HanzoRazer/luthiers-toolbox) - Main repository with templates and documentation
- [Express Edition](https://github.com/HanzoRazer/ltb-express)
- [Pro Edition](https://github.com/HanzoRazer/ltb-pro)
- [Enterprise Edition](https://github.com/HanzoRazer/ltb-enterprise)

## License

Copyright © 2025 Luthier's ToolBox Project
