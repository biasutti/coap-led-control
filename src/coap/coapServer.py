import asyncio
import logging

import aiocoap
import aiocoap.resource as resource

# logging setup
from src.coap.resource.LEDResource import LEDResource
from src.coap.resource.examples.BlockResource import BlockResource
from src.coap.resource.examples.SeparateLargeResource import SeparateLargeResource
from src.coap.resource.examples.TimeResource import TimeResource
from src.coap.resource.examples.WhoAmIResource import WhoAmIResource

logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)

def main():
    # Resource tree creation
    root = resource.Site()

    root.add_resource(['.well-known', 'core'], resource.WKCResource(root.get_resources_as_linkheader, None))

    # Example resources
    root.add_resource(['examples', 'time'], TimeResource())
    root.add_resource(['examples', 'block'], BlockResource())
    root.add_resource(['examples', 'separate'], SeparateLargeResource())
    root.add_resource(['examples', 'whoami'], WhoAmIResource())

    # Own resources
    root.add_resource(['dsiot', 'led-01'], LEDResource())

    asyncio.Task(aiocoap.Context.create_server_context(root))
    asyncio.get_event_loop().run_forever()

def start_coap_server():
    main()