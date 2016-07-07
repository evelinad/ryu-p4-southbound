

class CounterArray(object):

    def __init__(self, name, counter_id):
        super(CounterArray, self).__init__()
        self.name = name
        self.counter_id = counter_id
        self.is_direct = None
        self.size = None
        self.binding = None
