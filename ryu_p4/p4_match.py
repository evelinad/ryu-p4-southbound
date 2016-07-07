
class P4MatchKey(object):

    def __init__(self, field_name, match_type, bitwidth):
        super(P4MatchKey, self).__init__()
        self.field_name = field_name
        self.match_type = match_type
        self.bitwidth = bitwidth

class P4MatchType(object):
    '''
    From original repo:
    https://github.com/p4lang/behavioral-model
    '''
    EXACT = 0
    LPM = 1
    TERNARY = 2
    VALID = 3 # not yet supported

    @staticmethod
    def to_str(x):
        return {0: "exact", 1: "lpm", 2: "ternary", 3: "valid"}[x]

    @staticmethod
    def from_str(x):
        return {"exact": 0, "lpm": 1, "ternary": 2, "valid": 3}[x]
