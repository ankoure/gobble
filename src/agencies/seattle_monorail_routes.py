"""
SEATTLE_MONORAIL route constants.

Auto-generated from GTFS Static data. Do not manually edit.
Regenerate using: python generate_agency_routes.py <gtfs_zip> seattle_monorail
"""

BUS_STOPS = {}

# SEATTLE_MONORAIL Bus routes
ROUTES_BUS = set(BUS_STOPS.keys())

# SEATTLE_MONORAIL Commuter Rail/Regional Rail lines
ROUTES_CR = {"SCM"}

# SEATTLE_MONORAIL Rapid Transit routes
ROUTES_RAPID = set()


ALL_ROUTES = ROUTES_BUS.union(ROUTES_CR).union(ROUTES_RAPID)
