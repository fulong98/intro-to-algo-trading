from ibapi.client import EClient
from ibapi.wrapper import EWrapper  
"""
EClient: handle all outgoing data
EWrapper: handle all incoming data
"""
class IBapi(EWrapper, EClient):
     def __init__(self):
         EClient.__init__(self, self) 

app = IBapi()
app.connect('127.0.0.1', 4002, 123)
app.run()
import time
time.sleep(2)
app.disconnect()