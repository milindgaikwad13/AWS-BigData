


directory_in_str = ''

import urllib
from smb.SMBHandler import SMBHandler
from smb.SMBConnection import SMBConnection
conn = SMBConnection(userID, password, client_machine_name, server_name, use_ntlm_v2 = True)
assert conn.connect(server_ip, 139)

fileList = conn.listPath('','/')

print(fileList)