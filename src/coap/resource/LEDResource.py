import aiocoap
import aiocoap.resource as resource

class LEDResource(resource.Resource):

    def __init__(self, led):
        super().__init__()
        self.led = led

    async def render_get(self, request):
        if self.led.power_state:
            payload = "LED is ON"
        else:
            payload = "LED is OFF"

        return aiocoap.Message(content_format=0,
                payload=payload.encode('utf8'))