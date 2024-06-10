import time

# get current time
seconds = time.time()
# print seconds since epoch
print(f"Seconds since January 1, 1970: {seconds:,} or {seconds:.2e} in scientific notation")

# for second print
local_time = time.localtime(seconds)
print(time.strftime("%b %d %Y", local_time))