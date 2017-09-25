class Door:
    def __init__(self):
        self._open = False
    
    def _get_state(self):
        return "open" if self._open else "closed"
    
    def toggle(self):
        self._open = not self._open
        print(self._get_state())