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
import random
import string


# --------------------------------------------------------------------------
# GET: /
# --------------------------------------------------------------------------
@app.route('/generator/random_string/<size>', methods=['GET'])
async def get_random_string(request, size):
    logger.info('Resource Requested: {}'.format(request.url))
    letters = string.ascii_lowercase
    result = ''.join(random.choice(letters) for i in range(int(size)))

    return json(
        {
            "result": result
        }
    )
