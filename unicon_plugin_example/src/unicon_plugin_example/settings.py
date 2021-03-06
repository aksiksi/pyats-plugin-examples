'''
Connection Settings
-------------------

Connection settings are basically various key/value pairs that controls the
default behavior of a connection. 

'''

from unicon.plugins.generic.settings import GenericSettings

class OrzSettings(GenericSettings):
 
    def __init__(self):
        # inherit any parent settings
        super().__init__()

        # and modify some for our own
        self.CONNECTION_TIMEOUT = 60*5

        # and we could add more - to be used in plugins if needed
        # self.<keyword> = <value>