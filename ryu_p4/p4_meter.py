

MeterType = enum('MeterType', 'packets', 'bytes')

class P4MeterArray(object):

    def __init__(self, name, meter_id):
        super(P4MeterArray, self).__init__()
        self.name = name
        self.meter_id = meter_id
        self.type = None
        self.is_direct = None
        self.size = None
        self.binding = None
        self.rate_count = None
