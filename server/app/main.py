# ltb-fingerboard-designer - Server Entry Point
# Extract features from golden master as needed
# Golden Master: https://github.com/HanzoRazer/luthiers-toolbox

from fastapi import FastAPI

app = FastAPI(
    title=""LTB Fingerboard Designer - Fingerboard radius, scale, and multiscale calculator"",
    version=""0.1.0""
)

@app.get("/")
def read_root():
    return {"status": "ready", "edition": "FINGERBOARD_DESIGNER"}
