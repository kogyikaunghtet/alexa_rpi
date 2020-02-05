import time
class debounce_handler(object):
    DEBOUNCE_SECONDS = 0.3
    def __init__(self):
        self.lastEcho = time.time()
    def on(self, client_address, name):
        if self.debounce():
            return True
        return self.act(client_address, True, name)
    def off(self, client_address, name):
        if self.debounce():
            return True
        return self.act(client_address, False, name)
    def act(self, client_address, state):
        pass
    def debounce(self):
        if (time.time() - self.lastEcho) < self.DEBOUNCE_SECONDS:
            return True
        self.lastEcho = time.time()
        return False


