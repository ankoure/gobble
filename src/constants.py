"""
Route constants - loaded from config/routes.json at startup.

This module loads route constants (BUS_STOPS, ROUTES_BUS, ROUTES_CR, ROUTES_RAPID, ALL_ROUTES)
from config/routes.json, which should be mounted as a Kubernetes ConfigMap.
Each set of constants correlates a GTFS Static, and GTFS-RT pair.
For example SEPTA maintains seperate GTFS bundles for Regional Rail and Bus/Trolley.

Generate routes.json with:
    python scripts/generate_agency_routes.py <gtfs_zip_or_url> <agency> --format json
"""

import json
from pathlib import Path

from config import CONFIG

AGENCY = CONFIG.get("agency", "mbta").lower()

_ROUTES_FILE = Path("config/routes.json")

if not _ROUTES_FILE.exists():
    raise FileNotFoundError(
        f"config/routes.json not found. "
        f"Generate it with: python scripts/generate_agency_routes.py <gtfs_zip> {AGENCY} --format json"
    )

_data = json.loads(_ROUTES_FILE.read_text())
BUS_STOPS = {k: set(v) for k, v in _data["bus_stops"].items()}
ROUTES_CR = set(_data.get("routes_cr", []))
ROUTES_RAPID = set(_data.get("routes_rapid", []))
ROUTES_BUS = set(BUS_STOPS.keys())
ALL_ROUTES = ROUTES_BUS | ROUTES_CR | ROUTES_RAPID
