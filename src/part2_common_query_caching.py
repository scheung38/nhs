from riak import RiakClient, RiakBucket, RiakObject, RiakKeyFilter, RiakNode

import re
from src.part1_news_search import my_query, get_directory

import pandas as pd


df = pd.read_table('../hscicNews',
                       sep='/n',
                   skiprows=0,
                   skipfooter=0,
                   )


print("df is: {0}".format(df))
print("test")
print("df is: {0}".format(df.to_dict()))





# client = RiakClient(pb_port=8087, protocol='pbc')

# Single Node
# client = RiakClient(protocol='http', host='127.0.0.1', http_port=8098)

# A Cluster of Nodes
client = RiakClient(nodes=[{'host': '127.0.0.1', 'http_port': 8098}])

# bucket = client.bucket_type('news').bucket('hscicNews')
bucket = client.bucket_type('news').bucket('hscicNews')

custom_search = ['Care|Quality|Commission', 'September|2004', 'general|population|generally',
                 'Care Quality Commission|admission', 'general population|Alzheimer']

val = []

for x, i in enumerate(custom_search, 0):
    regex = re.compile(i)
    val.append(my_query(regex, get_directory()))

keys = bucket.new('RESULT', data=df.to_dict())

# Secondary Indexes
keys.add_index("bmonth_bin", 'April')
keys.add_index("byear_int", 2013)

keys.store()

janes_orders = bucket.get_index("bmonth_bin", 'April')
print(janes_orders.results)


print("this is val stored: ", val)
print("this is len of val: ", len(val))

# Secondary Indexes
# for i in range(0, len(val)):
#     order = bucket.get(str(i))
#     order.add_index(custom_search[0], "April")  # custom_search[i]
#     # order.store()
#     print(i)
#
#
#
# keys.add_index("fname_bin", "Sean")
# keys.add_index("byear_int", 1979)
# keys.store()
#
# # Performs an equality query
# keys = bucket.get_index("fname_bin", "Sean")
#
# # Performs a range query
# eighties = bucket.get_index("byear_int", 1980, 1989)

# val2 = "two"
# key2 = bucket.new('two', data=val2)
# key2.store()
#
# val3 = {"myValue": 3}
# key3 = bucket.new('three', data=val3)
# key3.store()
#
# print(client)
#
# fetched1 = bucket.get('one')
# fetched2 = bucket.get('two')
# fetched3 = bucket.get('three')
#
# print(fetched1.data)
# print(fetched2.data)
# print(fetched3.data)
#
# print('Value 1 correct: ' + str(val1 == fetched1.data))
# print('Value 2 correct: ' + str(val2 == fetched2.data))
# print('Value 3 correct: ' + str(val3 == fetched3.data))

# assert val1 == fetched1.data
# assert val2 == fetched2.data
# assert val3 == fetched3.data
