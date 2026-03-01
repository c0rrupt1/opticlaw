class Tool:
    """Base class for tools"""

    def __init__(self, manager):
        self.channel = None # gets replaced by current channel by the manager
        self.manager = manager

    def result(self, data, success=True):
        """unified way of returning tool results"""
        return {
            "status": "success" if success else "error",
            "content": data
        }
