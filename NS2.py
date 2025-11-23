import snap7
from snap7.util import get_bool, get_sint, set_sint, set_bool

client = snap7.client.Client()

# Conectar al PLC S7-1500 (rack 0, slot 1)
client.connect("10.72.101.72", 0, 1)

# Leemos DB1, desde offset 0, 256 bytes
data = client.db_read(1, 0, 255)

print("RAW DATA:", data)

# Siemens STRING: [MaxLen][CurrentLen][Text...]

# Byte 6 user and password

set_bool(data, 0, 0, True)
set_sint(data, 3, 1)  # ON
set_sint(data, 5, 2)  # OFF

# print("User/Password:", get_string(data, 6))
print("LED:", get_bool(data, 0, 0))
print("ON:", get_sint(data, 3))
print("OFF:", get_sint(data, 5))

client.db_write(1, 0, data)
client.disconnect()
