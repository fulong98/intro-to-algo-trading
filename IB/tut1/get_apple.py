from ibapi.contract import Contract
from ibapi.client import EClient
from ibapi.wrapper import EWrapper 
import threading
import time


class IBapi(EWrapper, EClient):
	def __init__(self):
		EClient.__init__(self, self)
	def tickPrice(self, reqId, tickType, price, attrib):
		if tickType == 2 and reqId == 1:
			print('The current ask price is: ', price)

def run_loop():
	app.run()

app = IBapi()
app.connect('127.0.0.1', 4002, 123)

#Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

time.sleep(1) #Sleep interval to allow time for connection to server

#Create contract object
apple_contract = Contract()
apple_contract.symbol = 'AAPL'
apple_contract.secType = 'STK'
apple_contract.exchange = 'SMART'
apple_contract.currency = 'USD'

#Request Market Data
app.reqHistoricalData(1, apple_contract, '', '2 D', '1 hour', 'BID', 0, 2, False, [])
# riq, contract object, ticktype, unsubscribed snapshot, subscribed snapshot, internal use


#Working with Pandas DataFrames
import pandas

df = pandas.DataFrame(app.data, columns=['DateTime', 'Close'])
df['DateTime'] = pandas.to_datetime(df['DateTime'],unit='s') 
df.to_csv('APPL_hourly.csv')  

print(df)
time.sleep(10) #Sleep interval to allow time for incoming price data
app.disconnect()