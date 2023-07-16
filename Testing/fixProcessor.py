from datetime import datetime, timedelta
import sys
import json
import pandas

time_format = '%Y%m%d-%H:%M:%S.%f'

file_path = ''  # Replace with the actual file path

class CustomDateTime(datetime):
    def __str__(self):
        return self.strftime('%Y-%m-%d %H:%M:%S')
    
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

EXEC_REPORT = '35=8'
NEW_ORDER = '35=D'
CANCEL = '35=F'

NEW_ER = '150=0'
TRADE_ER = '150=F'
CANCEL_ER = '150=4'

COID_PFX = '11='
CCLOID_PFX = '41='
DELIMITER = '\x01'
SND_TM_PFX = '52='
TX_TM_PFX = '60='

'''
Data structure = 
{ 
    'orderId' : 
    {
        out: timestamp,
        new: timestamp,
        new_transact: timestamp,
        trade: timestamp,
        trade_transact: timestamp
        cancel_out: timestamp
        cancel_in: timestamp
        cancel_transact: timestamp
    }
}

'''

# Open the file in read mode
count = 0
noneCount = 0
with open(file_path, 'r') as logs:
    orders = []
    orderData = {}    
    try: 
        for line in logs:
            position = line.find(COID_PFX)
            timestamp = line.find(SND_TM_PFX)
            if position == -1 or timestamp == -1:
                continue
            id = line[position+3:position+39]

            cancelposition = line.find(CCLOID_PFX)
            cancelid = line[cancelposition+3:cancelposition+39]

            time = CustomDateTime.strptime(line[timestamp+3: timestamp + 24], time_format)
            if NEW_ORDER in line:
                orders.append(id)
                orderData[id] = {'out' :  time }
                count +=1
            elif EXEC_REPORT in line:
                timestamp = line.find(TX_TM_PFX)
                tx_time = CustomDateTime.strptime(line[timestamp+3: timestamp + 24], time_format)
                if orderData.get(id) == None and orderData.get(cancelid) == None:
                    noneCount += 1
                elif NEW_ER in line:
                    orderData[id]['new'] = time
                    orderData[id]['new_transact'] = tx_time
                elif CANCEL_ER in line:
                    orderData[cancelid]['cancel_in'] = time
                    orderData[cancelid]['cancel_transact'] = tx_time
                elif TRADE_ER in line:
                    orderData[id]['trade'] = time
                    orderData[id]['trade_transact'] = tx_time
                else: 
                    orderData[id]['reject'] = time
                    orderData[id]['reject_transact'] = tx_time
            elif CANCEL in line:
                orderData[cancelid]['cancel_out'] = time

    except Exception as e: 
        print("ERROR: ", e)
#print(orderData)
print("Processed Orders: ", count)
print("Orders with no reference (not processed): ", noneCount)

fastestNew = sys.maxsize
slowestNew = 0
newTimeTotal = 0
newTimes = []

fastestNewTransact = sys.maxsize
slowestNewTransact = 0
newTransactTimeTotal= 0

fastestCancel = sys.maxsize
slowestCancel = 0
cancelTimeTotal = 0
cancelCount = 0
missedCancel = 0
cancelTimes = []


def timedelta_to_milliseconds(td):
    milliseconds = td.days * 24 * 60 * 60 * 1000 + td.seconds * 1000 + td.microseconds / 1000
    return int(milliseconds)

for i in orders:
    #print(i)
    transactTime = timedelta_to_milliseconds(orderData[i]['new_transact'] - orderData[i]['out'])
    time = timedelta_to_milliseconds(orderData[i]['new'] - orderData[i]['out'])
    if orderData[i].get('cancel_in') != None:
        cancelTime = timedelta_to_milliseconds(orderData[i]['cancel_in'] - orderData[i]['cancel_out'])
        #Cancel Time Processing 
        if cancelTime < 0:
            print ("Cancel ER before instruction: ", orderData[i])
        if cancelTime < fastestCancel:
            fastestCancel = cancelTime
        if time > slowestCancel:
            slowestCancel = cancelTime
        cancelTimeTotal += cancelTime
        cancelCount += 1
        cancelTimes.append(cancelTime)

    else:
        missedCancel += 1
    #Transact time processing
    if transactTime < 0:
        print ("Transact ER before instruction: ", orderData[i])
    if transactTime < fastestNewTransact:
        fastestNewTransact = transactTime
    if transactTime > slowestNewTransact:
        slowestNewTransact = transactTime
    newTransactTimeTotal += transactTime

    #New time processing
    if time < 0:
        print ("New ER before instruction: ", orderData[i])
    if time < fastestNew:
        fastestNew = time
    if time > slowestNew:
        slowestNew = time
    newTimeTotal += time
    newTimes.append(time)


#print(newTransactTimeTotal)
print("\n\n======= NEW ERs ======")
print("Fastest NEW (ms): ", fastestNew)
print("Slowest NEW (ms): ", slowestNew)
print("Average Transact (ms): ", newTransactTimeTotal/len(orders))
print("Average New (ms): ", newTimeTotal/len(orders))
newTimes.sort()
nineFifth = newTimes[int(len(newTimes)*.95)]
print("95th Percentile is: ", nineFifth)

print("\n\n======= Cancel ERs ======")
print("Fastest CANCEL (ms): ", fastestCancel)
print("Slowest CANCEL (ms): ", slowestCancel)
print("Missed cancel: ",missedCancel)
print("Processed IDs: ", len(orderData))
#print("Processed Data: ", len(orders))
print("Average Cancel (ms): ", cancelTimeTotal/cancelCount)
cancelTimes.sort()
nineFifth = cancelTimes[int(len(cancelTimes)*.95)]
print("95th Percentile is: ", nineFifth)

print("\n\nProcessed: ", len(orderData))

with open (file_path + '.json', 'w') as save_file:
    json.dump(json.dumps(orderData, cls=DateTimeEncoder), save_file)

data = pandas.read_json(json.dumps(orderData, cls=DateTimeEncoder))
data.to_excel( file_path + ".xlsx", index=False)