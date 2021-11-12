import asyncio
import logging

import aiocoap
import aiocoap.resource as resource

# logging setup
from coap.resource.HealthResource import HealthResource
from coap.resource.LEDResource import LEDResource
from coap.resource.examples.BlockResource import BlockResource
from coap.resource.examples.SeparateLargeResource import SeparateLargeResource
from coap.resource.examples.TimeResource import TimeResource
from coap.resource.examples.WhoAmIResource import WhoAmIResource

logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)

root = None

# TODO: Create class object for coapServer
def setup():
    # Resource tree creation
    global root
    root = resource.Site()

    root.add_resource(['.well-known', 'core'], resource.WKCResource(root.get_resources_as_linkheader, None))

    # Example resources
    root.add_resource(['examples', 'time'], TimeResource())
    root.add_resource(['examples', 'block'], BlockResource())
    root.add_resource(['examples', 'separate'], SeparateLargeResource())
    root.add_resource(['examples', 'whoami'], WhoAmIResource())


def add_led_resource(led):
    # Own resources
    global root
    root.add_resource(['dsiot', led.name], LEDResource(led))


def start_coap_server(sensors):
    root.add_resource(['dsiot', 'health'], HealthResource(sensors))
    asyncio.Task(aiocoap.Context.create_server_context(root))
    asyncio.get_event_loop().run_forever()


def setup_coap_server():
    setup()
