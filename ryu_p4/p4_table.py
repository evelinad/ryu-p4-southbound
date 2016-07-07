
TableType = enum('TableType', 'simple', 'indirect', 'indirect_ws')

class P4Table(object):

    def __init__(self, table_name, table_id):
        super(P4Table, self).__init__()

        # table information from json
        self.table_name = table_name
        self.table_id = table_id
        self.match_type = None
        self.type = None
        self.actions = {}  # action name => P4Action
        self.key = []  # match keys (P4MatchKey)
        self.default_action = None  # P4Action

    def num_key_fields(self):
        return len(self.key)
