Example for Configuring a Command Assistant for Automatic Health Check
======================================================================

Example for Configuring a Command Assistant for Automatic Health Check

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001564005297__fig_dc_vrp_ops_cfg_new_001601), the remote server is an SFTP server. DeviceA and the SFTP server have reachable routes to each other. To reduce maintenance workload, configure DeviceA to automatically collect daily health information.**Figure 1** Network diagram of automatic health check using commands![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001512685918.png)


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a command assistant and set a timer as the trigger condition for the assistant, so that the assistant performs a health check periodically.
2. Specify the commands that the command assistant runs to collect health information.


#### Procedure

1. Configure a command assistant.
   
   
   
   # Create a command assistant and configure it to run at 01:00 a.m. every day.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] ops
   [~DeviceA-ops] assistant collect_health
   [*DeviceA-ops-assistant-collect_health] condition timer cron 0 1 * * * *
   [*DeviceA-ops-assistant-collect_health] commit
   ```
   
   # Specify the commands that the command assistant runs to collect information, such as the hardware status, route status, and interface link status, configure the device to save the collected information to a file.
   
   ```
   [~DeviceA-ops-assistant-collect_health] execute 1 command display device > health.txt
   [*DeviceA-ops-assistant-collect_health] execute 1.5 command display health >> health.txt
   [*DeviceA-ops-assistant-collect_health] execute 2 command display ip routing-table >> health.txt
   [*DeviceA-ops-assistant-collect_health] execute 2.5 command display lldp neighbor brief >> health.txt
   [*DeviceA-ops-assistant-collect_health] commit
   [~DeviceA-ops-assistant-collect_health] return
   ```
2. Configure an IP address for the specified interface.
   
   
   ```
   <DeviceA> system-view
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.1.1.1 24
   [*DeviceA-100GE1/0/1] commit
   [~DeviceA-100GE1/0/1] quit
   ```

#### Verifying the Configuration

# Check the configuration of the command assistant.

```
<DeviceA> display ops assistant verbose name collect_health
Assistant information                                                           
  Name                 : collect_health                                         
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
  Task abstract        : display device > health.txt; display health >> health.txt; display ip routing-table >> health.txt; display lldp
neighbor brief >> health.txt;
```

#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  ops
   assistant collect_health
    execute 1 command display device > health.txt
    execute 1.5 command display health >> health.txt
    execute 2 command display ip routing-table >> health.txt
    execute 2.5 command display lldp neighbor brief >> health.txt
    condition timer cron 0 1 * * * *
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
  #
  ```