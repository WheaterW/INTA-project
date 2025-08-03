Example for Configuring EVA Based on Python Scripts
===================================================

Example for Configuring EVA Based on Python Scripts

#### Networking Requirements

A customized Python script is stored on an SFTP server. O&M personnel want to use EVA to monitor the CPU usage and memory usage. The Python script specifies that when the CPU usage and memory usage exceed 90%, the system automatically generates an alarm log reporting high CPU and memory usages, prompting O&M personnel to maintain devices in a timely manner.

**Figure 1** Networking diagram of monitoring CPU usage changes through EVA  
![](../images/en-us_image_0000001534107514.png)

#### Configuration Roadmap

1. Subscribe to telemetry data based on the gRPC service.
2. Compile a Python script to customize events and troubleshooting strategies.
3. Upload the Python script to the device.
4. Install the Python script.
5. Register the Python script.

#### Procedure

1. Subscribe to telemetry data based on the gRPC service.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] grpc
   [~DeviceA-grpc] grpc server
   [~DeviceA-grpc-server] source-ip 0.0.0.0
   [*DeviceA-grpc-server] [server-port](cmdqueryname=server-port) 57400
   [*DeviceA-grpc-server] server enable
   [*DeviceA-grpc-server] quit
   [*DeviceA-grpc] quit
   [*DeviceA] commit
   ```
2. Compile a Python script to customize events and troubleshooting strategies.
   
   
   
   # Compile the script **cpuMemHigh.py** to subscribe to the system CPU usage and memory usage, and calculate the average values of last 10 CPU usages and memory usages. If both the average values exceed 90%, an alarm log is generated.
   
   ```
   import eva
   def condition(): 
       e1 = eva.Event()
       kpi1 = e1.addkpi("huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info/system-cpu-usage")
       e1.ret = eva.avg(kpi1, 10) > 90
    
       e2 = eva.Event()
       kpi2 = e2.addkpi("huawei-cpu-memory:cpu-memory/board-memory-infos/board-memory-info/os-memory-usage")
       e2.ret = eva.avg(kpi2, 10) > 90
       
       s1 = eva.Strategy()
       s1.formula = e1 & e2
       s1.validTime= 10
       action1 = eva.log("board ${e1.slot-id}--${e1.cpu-id} cpu and memory simultaneously overload")
       s1.addaction(action1)
   ```
3. Upload the Python script to the device.
   
   
   
   # Configure DeviceA functioning as an SFTP client to download the Python script file **cpuMemHigh.py** from the SFTP server. For details, see "Managing Files Using SFTP" in Configuration Guide > Basic Configuration > File System Management Configuration.
   
   ```
   [~DeviceA] sftp client-transfile get host-ip 10.2.1.1 username client001 password Helloworld@6789 sourcefile cpuMemHigh.py
   Trying 10.2.1.1 ... 
   Press CTRL+K to abort 
   Connected to 10.2.1.1 ... 
   Remote file: /cpuMemHigh.py --->  Local file: /cpuMemHigh.py 
   Downloading the file. Please wait.. 
   Downloading file successfully ended.   
   File download is completed in 1 seconds. 
   [~DeviceA] [quit](cmdqueryname=quit)
   ```
4. Install the Python script.
   
   
   ```
   <DeviceA> ops install file cpuMemHigh.py
   ```
5. Register the Python script.
   
   
   ```
   <DeviceA> ops run python evamain.py install cpuMemHigh.py
   ```

#### Verifying the Configuration

# Display strategy registration information of the device.

```
<DeviceA> display eva register-strategy cpuMemHigh.py
Total: 1 
-----------------------------------------------------------------------------------------
FileName   Name   ValidTime SurvivalTime SecDetect RegisterTime         Action Formula   
-----------------------------------------------------------------------------------------
cpuMemHigh.py s1            10           60 False     2020-5-14 11:12:21  log    e1&&e2    
-----------------------------------------------------------------------------------------   
```

# Display registration information about the event configured in the script.

```
<DeviceA> display eva register-events cpuMemHigh.py 
Total: 2                   
----------------------------------------------------------------------------
FileName   EventName   Compare   Threshold  Frequency Xpath                 
----------------------------------------------------------------------------
cpuMemHigh.py    e1        >             90          1     huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info/system-cpu-usage  
cpuMemHigh.py    e2        >             90          1     huawei-cpu-memory:cpu-memory/board-memory-infos/board-memory-info/os-memory-usage 
----------------------------------------------------------------------------
```

#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  grpc
   #
   grpc server                                                                    
    source-ip 0.0.0.0 
    server-port 57400
    server enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
  #
  ```