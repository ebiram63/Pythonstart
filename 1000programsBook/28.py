# The app displays the os is 32 or 64 bits

import struct 
print(struct.calcsize("P") * 8)
