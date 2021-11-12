import json

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


    '''
    default payload:
    {
        state: 1 or 0
    }
    '''
    async def render_post(self, request):
        if request.payload is not None:
            payload = str(request.payload.decode("utf-8"))
            #payload = '{"state": 1}'
            data = json.loads(payload)
            if data['state']:
                self.led.on()
            else:
                self.led.off()

            return aiocoap.Message(content_format=0,
                                   code=204,
                                   payload="test-post".encode('utf8'))
        return aiocoap.Message(content_format=0,
                               code=404,
                               payload="test-post-error".encode('utf8'))
