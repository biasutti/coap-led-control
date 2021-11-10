import aiocoap
import aiocoap.resource as resource

class LEDResource(resource.Resource):

    def __init__(self, led):
        super().__init__()
        self.led = led

    async def render_get(self, request):
        return aiocoap.Message(content_format=0,
                payload="LED-Resource".encode('utf8'))