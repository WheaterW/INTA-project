Example for Configuring a Script Assistant for Automatic Backup of DHCP Snooping Binding Tables to a Remote Server
==================================================================================================================

Example for Configuring a Script Assistant for Automatic Backup of DHCP Snooping Binding Tables to a Remote Server

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001513165026__fig_dc_vrp_ops_cfg_new_001701), the remote server is an SFTP server. DeviceA and the SFTP server have reachable routes to each other. The device is required to back up DHCP snooping binding tables to the remote SFTP server.**Figure 1** Networking diagram for configuring automatic backup of DHCP snooping binding tables to a remote server  
![](figure/en-us_image_0000001513165050.png)


#### Procedure

1. Compile Python scripts.
   
   
   
   # Compile two Python scripts: SnpTblBakRmtPut.py and SnpTblBakRmtGet.py.
   
   In the SnpTblBakRmtGet.py script, set the execution of the script assistant to be triggered by a timer. In the SnpTblBakRmtPut.py script, set the execution of the script assistant to be triggered by a log.
   
   * The SnpTblBakRmtGet.py script is as follows:
     ```
     #!/usr/bin/env python
     # -*- coding: utf-8 -*-
     #
     # Copyright (C) Huawei Technologies Co., Ltd. 2021-2030. All rights reserved.
     
     import re
     import string
     import http.client
     import ops
     import sys, re, os, time
     
     # Variable parameters
     serverIpPara = "10.2.1.1"                     # IP address of the remote server.
     serverPortPara = "22"                       # Port number of the remote server. The port number of the SFTP server is fixed to 22.
     userNamePara = "huawei"                     # Username for logging in to the remote server.
     passWordPara = "YsHsjx_202206"                   # Password for logging in to the remote server.
     remotePathPara = "dhcpsnp.tbl"                 # Name of the backup file stored on the remote server.
     localPathPara = "flash:/dhcpsnprmt.tbl"        # Name of the file downloaded from the remote server to the local device. This name must be different from the name of the local backup file to avoid overwriting the existing local file.
     recoverFileNamePara = "flash:/dhcpsnprmt.tbl"        # Specify the file name used for a restored DHCP snooping binding table.
     # Variable parameters
     
     yang_func_ret_err = lambda ret, rsp_data: f'yang function returns {ret} and rsp_data: {rsp_data}'
     yang_func_ret_success = 'SUCCESS'
     yang_func_ret_not_found = 'NOT FOUND'
     
     # error code
     OK = 0
     ERR = 1
     
     def ops_conn_operation(func):
         def wapper(*args, **kwargs):
             ops_conn = ops.OPSConnection("localhost")
             kwargs.update({"ops_conn": ops_conn})
             try:
                 ret = func(*args, **kwargs)
                 return ret
             except Exception as reason:
                 exception_info = \
                     "{} failed, reason = {}".format(func.__name__, reason)
                 raise Exception(exception_info)
             finally:
                 ops_conn.close()
         return wapper
     
     def ops_return_result(ret):
         return ((ret != http.client.OK) and \
                 (ret != http.client.CREATED) and \
                 (ret != http.client.NO_CONTENT))
     
     @ops_conn_operation
     def download_file_by_sftp(ops_conn=None):
     
             uri = '{}'.format('/restconf/operations/huawei-sshc:ssh-transfer-file')
             # Do not change the sequence of options between <input> and </input>. Otherwise, the operation may fail.
             req_template = string.Template('''
                 <input>
                     <server-port>$serverPort</server-port>
                     <host-addr-ipv4>$serverIp</host-addr-ipv4>
                     <command-type>get</command-type>
                     <user-name>$userName</user-name>
                     <password>$password</password>
                     <local-file-name>$localPath</local-file-name>
                     <remote-file-name>$remotePath</remote-file-name>
                 </input>
                 ''')
             req_data = req_template.substitute(serverIp=serverIpPara, 
                                                serverPort=serverPortPara, 
                                                userName=userNamePara, 
                                                password=passWordPara, 
                                                remotePath=remotePathPara, 
                                                localPath=localPathPara)
             ret, _, rsp_data = ops_conn.create(uri, req_data)
             if ops_return_result(ret):
                 print(rsp_data)
                 return ERR, yang_func_ret_err(ret, rsp_data)
             return OK, yang_func_ret_success
     
     @ops_conn_operation
     def recover_file(ops_conn=None):
     
             uri = '{}'.format('/restconf/operations/huawei-dhcp:recover-user-bind-table')
             # Do not change the sequence of options between <input> and </input>. Otherwise, the operation may fail.
             req_template = string.Template('''
                 <input>
                     <user-bind-file-name>$usrBindTblFileName</user-bind-file-name>
                 </input>
                 ''')
             req_data = req_template.substitute(usrBindTblFileName=recoverFileNamePara)
             ret, _, rsp_data = ops_conn.create(uri, req_data)
             if ops_return_result(ret):
                 print(rsp_data)
                 return ERR, yang_func_ret_err(ret, rsp_data)
             return OK, yang_func_ret_success
     
     if __name__ == "__main__":
         for i in range(10):
             ret, _ = download_file_by_sftp()
             if ret == OK:
                 recover_file()
                 break
     ```
   * The SnpTblBakRmtPut.py script is as follows:
     ```
     #!/usr/bin/env python
     # -*- coding: utf-8 -*-
     #
     # Copyright (C) Huawei Technologies Co., Ltd. 2021-2030. All rights reserved.
     
     import re
     import string
     import http.client
     import ops
     import sys, re, os, time
     
     # Variable parameters
     serverIpPara = "10.2.1.1"             # IP address of the remote server.
     serverPortPara = "22"               # Port number of the remote server. The port number of the SFTP server is fixed to 22.
     userNamePara = "huawei"               # Username for logging in to the remote server.
     passWordPara = "YsHsjx_202206"          # Password for logging in to the remote server.
     remotePathPara = "dhcpsnp.tbl"       # Name used to rename the local backup file after it is uploaded to the remote server.
     localPathPara = "flash:/dhcpsnp.tbl"       # Name of the local backup file to be uploaded to the remote server.
     # Variable parameters
     
     yang_func_ret_err = lambda ret, rsp_data: f'yang function returns {ret} and rsp_data: {rsp_data}'
     yang_func_ret_success = 'SUCCESS'
     yang_func_ret_not_found = 'NOT FOUND'
     
     # error code
     OK = 0
     ERR = 1
     
     def ops_conn_operation(func):
         def wapper(*args, **kwargs):
             ops_conn = ops.OPSConnection("localhost")
             kwargs.update({"ops_conn": ops_conn})
             try:
                 ret = func(*args, **kwargs)
                 return ret
             except Exception as reason:
                 exception_info = \
                     "{} failed, reason = {}".format(func.__name__, reason)
                 raise Exception(exception_info)
             finally:
                 ops_conn.close()
         return wapper
     
     def ops_return_result(ret):
         return ((ret != http.client.OK) and \
                 (ret != http.client.CREATED) and \
                 (ret != http.client.NO_CONTENT))
     
     @ops_conn_operation
     def upload_file_by_sftp(ops_conn=None):
     
             uri = '{}'.format('/restconf/operations/huawei-sshc:ssh-transfer-file')
             # Do not change the sequence of options between <input> and </input>. Otherwise, the operation may fail.
             req_template = string.Template('''
                 <input>
                     <server-port>$serverPort</server-port>
                     <host-addr-ipv4>$serverIp</host-addr-ipv4>
                     <command-type>put</command-type>
                     <user-name>$userName</user-name>
                     <password>$password</password>
                     <local-file-name>$localPath</local-file-name>
                     <remote-file-name>$remotePath</remote-file-name>
                 </input>
                 ''')
             req_data = req_template.substitute(serverIp=serverIpPara, 
                                                serverPort=serverPortPara, 
                                                userName=userNamePara, 
                                                password=passWordPara, 
                                                remotePath=remotePathPara, 
                                                localPath=localPathPara)
             ret, _, rsp_data = ops_conn.create(uri, req_data)
             if ops_return_result(ret):
                 print(rsp_data)
                 return ERR, yang_func_ret_err(ret, rsp_data)
             return OK, yang_func_ret_success
     
     if __name__ == "__main__":	
         upload_file_by_sftp()
     		
     ```
2. Upload and install the Python scripts.
   
   
   
   # Upload the SnpTblBakRmtPut.py and SnpTblBakRmtGet.py scripts to DeviceA, which functions as an SFTP client. (The Python scripts are stored on the SFTP client.)
   
   ```
   <HUAWEI> system-view
   [*HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [*DeviceA] sftp 10.3.1.1
   Trying 10.3.1.1 ... 
   Press CTRL+K to abort 
   Connected to 10.3.1.1 ... 
   Please input the username: client001
   Enter password: 
   sftp-client> get SnpTblBakRmtPut.py
   Warning: The file may not transfer correctly in ASCII mode.
   sftp-client> get SnpTblBakRmtGet.py
   Warning: The file may not transfer correctly in ASCII mode.
   sftp-client> quit
   ```
   
   # Install the Python scripts on DeviceA.
   
   ```
   <DeviceA> ops install file SnpTblBakRmtPut.py
   <DeviceA> ops install file SnpTblBakRmtGet.py
   ```
3. Configure script assistants.
   
   
   ```
   <DeviceA> system-view
   [*DeviceA] ops
   [*DeviceA-ops] assistant dhcpsnpget
   [*DeviceA-ops-assistant-dhcpsnpget] execute 1 python SnpTblBakRmtGet.py
   [*DeviceA-ops-assistant-dhcpsnpget] condition event feature dhcp name DHCPSNP_USERBINDTBL_RECOVER
   [*DeviceA-ops-assistant-dhcpsnpget] quit
   [*DeviceA-ops] assistant dhcpsnpput
   [*DeviceA-ops-assistant-dhcpsnpput] execute 1 python SnpTblBakRmtPut.py
   [*DeviceA-ops-assistant-dhcpsnpput] condition timer cron 0/30 * * * * *
   [*DeviceA-ops-assistant-dhcpsnpput] quit
   [*DeviceA-ops] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check the configuration of the script assistants.

```
<DeviceA> display ops assistant verbose name dhcpsnpget
Assistant information
  Name                 : dhcpsnpget
  State                : ready
  Type                 : command
  Default assistant    : no
 Running statistics
  Running times        : 0
  Queue size/(free)    : 10/(10)
  Skip for queue full  : 0
  Skip for delay       : 0
  Skip for suppression : 0
  Skip for error       : 0
 Execute information
  Task abstract        : SnpTblBakRmtGet.py 
 Trigger control
  Occurs threshold     : 1
  Period (s)           : 30
  Delay (s)            : 0
  Suppress max         : 0
  Hits in period       : 0
 Condition information
  Correlate expression : 
  Condition tag        : 
    Condition type     : event
    Subscribe result   : success
    Occurs threshold   : 0
    Period (s)         : 0
    Hits in period     : 0
```

#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  ops
   assistant dhcpsnpget
    execute 1 python SnpTblBakRmtGet.py 
    condition event feature dhcp name DHCPSNP_USERBINDTBL_RECOVER
   assistant dhcpsnpput
    execute 1 python SnpTblBakRmtPut.py 
    condition timer cron 0/30 * * * * *
  #
  return
  ```