Example for Configuring a Script Assistant for Automatic Health Check
=====================================================================

Example for Configuring a Script Assistant for Automatic Health Check

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001564125133__fig_dc_vrp_ops_cfg_new_001701), the remote server is an SFTP server. DeviceA and the SFTP server have reachable routes to each other. To reduce maintenance workload, configure DeviceA to automatically collect daily health information.**Figure 1** Networking diagram of automatic health check using a Python script![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001512685918.png)


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Compile, upload, and install a Python script on DeviceA.
2. Create a script assistant.


#### Procedure

1. Compile a Python script.
   
   
   
   # Compile a Python script named **health.py**.
   
   In the Python script, set the trigger condition as the timer and the task as executing commands to collect device information (including hardware status, route status, and interface link status) and to send the collected information to the SFTP server. The Python script is as follows:
   ```
   #!/usr/bin/env python
   # -*- coding: utf-8 -*-
   #
   # Copyright (C) Huawei Technologies Co., Ltd. 2021-2030. All rights reserved.
   
   import ops
   
   # Define the function for uploading a file to the SFTP server.
   def upload_file_by_sftp(server_addr, username, passwd, local_file, remote_file):
       # The parameters are described as follows.
       # server_addr: IP address of the SFTP server
       # username: username for logging in to the SFTP server
       # passwd: password for logging in to the SFTP server
       # local_file: file path on the device
       # remote_file: destination file path (path to which the file is uploaded on the SFTP server)
       ops_conn = ops.OPSConnection("localhost")
       uri = '{}'.format('/restconf/operations/huawei-sshc:ssh-transfer-file')
       req_data = '{}'.format(f'''
           <input>
               <server-port>22</server-port>
               <host-addr-ipv4>{server_addr}</host-addr-ipv4>
               <command-type>put</command-type>
               <user-name>{username}</user-name>
               <password>{passwd}</password>
               <local-file-name>{local_file}</local-file-name>
               <remote-file-name>{remote_file}</remote-file-name>
           </input>
       ''')
       ret, _, rsp_data = ops_conn.create(uri, req_data)
       ops_conn.close()
       return
   # Define the function of the trigger condition.
   def ops_condition(_ops):
   	_ops.timer.cron("con1","0 1 * * * *")      # Set the timer event.
   	_ops.correlate("con1")
   
   # Define the functions for tasks.
   def ops_execute(_ops):
           _ops.set_model_type("YANG")       # Configure the RESTful API to use the YANG model.
   	handle, err_desp  = _ops.cli.open()      # Enable the CLI channel.
   	_ops.cli.execute(handle,"display device > health.txt")      # Run the display device command, clear the health.txt file, and save the command output to the health.txt file.
   	_ops.cli.execute(handle,"display health >> health.txt")     # Run the display health command and add the command output to the health.txt file.
   	_ops.cli.execute(handle,"display ip routing-table >> health.txt")
   	_ops.cli.execute(handle,"display lldp neighbor brief >> health.txt")
   	ret = _ops.cli.close(handle)      # Close the CLI channel.
           upload_file_by_sftp("10.2.1.1", "user1", "password", "flash:/health.txt", "/usr1/logs/health.txt")    # Upload the file to the SFTP server. Specify the IP address, username, password, and other parameters in the upload_file_by_sftp function as required.
   	return 0
   
   ```
2. Upload and install the Python script.
   
   
   
   # Configure DeviceA functioning as an SFTP client to download the Python script file **health.py** from the SFTP server. The Python script is stored on the SFTP server.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] sftp 10.2.1.1
   Trying 10.2.1.1 ... 
   Press CTRL+K to abort 
   Connected to 10.2.1.1 ... 
   Please input the username:  
   Enter password: 
   sftp-client> get health.py
   Info: Transfer file in binary mode.
   Please wait for a while...
   /    635 bytes transferred
   Info: Downloaded the file successfully.
   ```
   
   # Install the Python script on DeviceA.
   
   ```
   [~DeviceA] quit
   <DeviceA> ops install file health.py
   ```
3. Configure a script assistant.
   
   
   ```
   <DeviceA> system-view
   [~DeviceA] ops
   [*DeviceA-ops] script-assistant python health.py
   [*DeviceA-ops] return
   [*DeviceA] commit
   ```
4. Configure an IP address for the specified interface on DeviceA.
   
   
   ```
   <DeviceA> system-view
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.1.1.1 24
   [*DeviceA-100GE1/0/1] commit
   [~DeviceA-100GE1/0/1] quit
   ```

#### Verifying the Configuration

# Check the configuration of the script assistant.

```
<DeviceA> display ops assistant verbose name health.py
Assistant information
  Name                 : health.py
  State                : ready
  Type                 : script
  Default assistant    : no
 Running statistics
  Running times        : 0
  Queue size/(free)    : 10/(10)
  Skip for queue full  : 0
  Skip for delay       : 0
  Skip for suppression : 0
  Skip for error       : 0
 Execute information
  Task abstract        : health.py : ops_execute()
 Trigger control
  Occurs threshold     : 1
  Period (s)           : 0
  Delay (s)            : 0
  Suppress max         : 0
  Hits in period       : 0
 Condition information
  Correlate expression : con1
  Condition tag        : con1
    Condition type     : timer
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
   script-assistant python health.py
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 24
  #
  ```