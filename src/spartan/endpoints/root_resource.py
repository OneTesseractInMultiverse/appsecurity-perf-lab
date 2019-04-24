from spartan import (
    app
)
from spartan.traffic_management import (
    list_routes
)
from sanic.response import (
    json
)
from sanic.log import (
    logger
)


# --------------------------------------------------------------------------
# GET: /
# --------------------------------------------------------------------------
@app.route('/', methods=['GET'])
async def get_root(request):
    logger.info('Resource Requested: {}'.format(request.url))
    return json(
        {
            "microservice_platform": "Spartan 2.0 - Async (Sanic)",
            "web_server": "Sanic",
            "ip_address": request.ip,
            "rules": list_routes()
        }
    )





