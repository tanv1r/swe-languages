# You want to operate on Unicode characters that have no specific encoding
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8') # decode: convert raw 8-bit values 
                                             # -> str
    else:
        value = bytes_or_str
    return value # Instance of str

# You want to operate on raw 8-bit values that are UTF-8 encoded characters (or
# some other encoding)
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8') # encode: convert unicode str 
                                             # -> raw 8-bit values
    else:
        value = bytes_or_str
    return value # Instance of bytes

# In Python3, writing to a binary file causes TypeError, because the encoding
# argument in open defaults to 'utf-8' which causes read and write operations 
# on file handles to expect unicode instances instead of byte instances 
# containing binary data
with open('random.bin', 'w') as f:
    f.write(os.urandom(10))
# The fix is to use 'wb' in open to indicate write binary data
with open('random.bin', 'wb') as f:
    f.write(os.urandom(10))
# For read it is 'rb'

# Things to remember:
# 1. In Python3, bytes contains 8-bit values; str contains unicode characters.
#    bytes and str instances cannot be used together with > or +
# 2. Use helper functions to ensure that the input you operate on are the type
#    of character sequence you expect: 8-bit values, utf-8 encoded characters,
#    unicode characters, etc.
# 3. To read/write binary data from/to a file, always open the file using rb/wb