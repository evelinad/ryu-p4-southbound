from ryu.base import app_manager

class P4Handler(app_manager.RyuApp):

    def __init__(self):
        super(P4Handler, self).__init__()
