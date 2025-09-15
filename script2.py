import time
epc=time.time()
print(epc)
local_time=time.localtime(epc)
print(local_time)
print(local_time.tm_zone)
print(local_time.tm_hour)
print(local_time.tm_sec)
print(local_time.tm_year)

