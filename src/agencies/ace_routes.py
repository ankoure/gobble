"""
ACE route constants.

Auto-generated from GTFS Static data. Do not manually edit.
Regenerate using: python generate_agency_routes.py <gtfs_zip> ACE
"""

BUS_STOPS = {
    "S": {"ARN", "COX", "RLN", "RSV", "SAC"},
    "SF": {"EMY", "SFC"},
}

# ACE Bus routes
ROUTES_BUS = set(BUS_STOPS.keys())

# ACE Commuter Rail/Regional Rail lines
ROUTES_CR = {"CC"}

# ACE Rapid Transit routes
ROUTES_RAPID = set()


ALL_ROUTES = ROUTES_BUS.union(ROUTES_CR).union(ROUTES_RAPID)
