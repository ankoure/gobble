"""
WSF route constants.

Auto-generated from GTFS Static data. Do not manually edit.
Regenerate using: python generate_agency_routes.py <gtfs_zip> wsf
"""

BUS_STOPS = {}

# WSF Bus routes
ROUTES_BUS = set(BUS_STOPS.keys())

# WSF Commuter Rail/Regional Rail lines
ROUTES_CR = set()

# WSF Rapid Transit routes
ROUTES_RAPID = set()


ALL_ROUTES = ROUTES_BUS.union(ROUTES_CR).union(ROUTES_RAPID)
