"""Télécharger les trois sources ; conserver les fichiers déjà présents."""
from pathlib import Path
from datetime import datetime, timezone
from zipfile import ZipFile
from io import BytesIO
import hashlib
import json
import requests

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
RAW.mkdir(parents=True, exist_ok=True)

SOURCES = {
    "ebp.csv": "https://www.federalreserve.gov/econres/notes/feds-notes/ebp_csv.csv",
    "vix.csv": "https://cdn-api.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv",
    "ff_daily.zip": "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip",
}
manifest_path = RAW / "download_manifest.json"
manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}

for filename, url in SOURCES.items():
    path = RAW / filename
    downloaded = not path.exists()
    if downloaded:
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        content = response.content
        if filename.endswith(".zip"):
            with ZipFile(BytesIO(content)) as archive:
                if archive.testzip() is not None:
                    raise ValueError("Archive ZIP endommagée")
        elif content.lstrip().startswith(b"<"):
            raise ValueError(f"Réponse HTML au lieu du CSV : {url}")
        path.write_bytes(content)

    content = path.read_bytes()
    checksum = hashlib.sha256(content).hexdigest()
    previous = manifest.get(filename, {})
    record = {
        "url": url,
        "bytes": len(content),
        "sha256": checksum,
        "downloaded_at_utc": (datetime.now(timezone.utc).isoformat()
                              if downloaded else previous.get("downloaded_at_utc")),
    }
    manifest[filename] = record
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"{filename}: {len(content):,} octets — prêt")

print("Données prêtes. Ouvrir notebooks/01_exploration.ipynb.")
