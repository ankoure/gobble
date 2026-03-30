"""
CAPMETRO route constants.

Auto-generated from GTFS Static data. Do not manually edit.
Regenerate using: python generate_agency_routes.py <gtfs_zip> capmetro
"""

BUS_STOPS = {}

# CAPMETRO Bus routes
ROUTES_BUS = set(BUS_STOPS.keys())

# CAPMETRO Commuter Rail/Regional Rail lines
ROUTES_CR = set()

# CAPMETRO Rapid Transit routes
ROUTES_RAPID = {"550"}


ALL_ROUTES = ROUTES_BUS.union(ROUTES_CR).union(ROUTES_RAPID)
