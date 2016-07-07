
class P4Action(object):

    def __init__(self, action_name, action_id):
        super(P4Action, self).__init__()
        self.action_name = action_name
        self.action_id = action_id
        self.runtime_data = []  # parameter

    def num_params(self):
        return len(self.runtime_data)

    def get_params(self):
        return runtime_data


class P4ActionRuntimeData(object):

    def __init__(self, name, bitwidth):
        self.name = name
        self.bitwidth = bitwidth
