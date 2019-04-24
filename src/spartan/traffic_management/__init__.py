from spartan import app


# -----------------------------------------------------------------------------
# FUNCTION LIST ROUTES
# -----------------------------------------------------------------------------
def list_routes():
    return [str(rule) for handler, (rule, router) in app.router.routes_names.items()]
