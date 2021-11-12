import json

import aiocoap
import aiocoap.resource as resource

import config


class HealthResource(resource.Resource):

    def __init__(self, sensors):
        super().__init__()
        self.sensors = sensors
        self.content = bytearray(self.render_content(), 'utf-8')

    async def render_get(self, request):
        return aiocoap.Message(payload=self.content)

    def render_content(self):
        data = {
            'name': config.DEVICE_NAME,
            'ipadress': ''
        }

        for sensor in self.sensors:
            sensor_data = {
                'name': sensor.name,
                'type': sensor.type
            }
            if sensor.type == 'binary':
                sensor_data_type = {
                    'power_state': sensor.power_state
                }
                sensor_data = {**sensor_data, **sensor_data_type}

            data = {**data, **sensor_data}

        payload = json.dumps(data)
        return payload
