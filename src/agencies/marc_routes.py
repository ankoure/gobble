"""
MARC route constants.

Auto-generated from GTFS Static data. Do not manually edit.
Regenerate using: python generate_agency_routes.py <gtfs_zip> marc
"""

BUS_STOPS = {}

# MARC Bus routes
ROUTES_BUS = set(BUS_STOPS.keys())

# MARC Commuter Rail/Regional Rail lines
ROUTES_CR = {"11704", "11705", "11706"}

# MARC Rapid Transit routes
ROUTES_RAPID = set()


ALL_ROUTES = ROUTES_BUS.union(ROUTES_CR).union(ROUTES_RAPID)
