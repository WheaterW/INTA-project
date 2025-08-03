Example for Configuring a Monitor Link Group
============================================

Example for Configuring a Monitor Link Group

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001176664425__fig5835174994419), downlink interfaces are required to detect an uplink failure and promptly adjust their interface status accordingly, to ensure network reliability.

**Figure 1** Network diagram of configuring a Monitor Link group![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 through interface 4 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, and 100GE 1/0/4, respectively.


  
![](figure/en-us_image_0000001130784672.png)
#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a Monitor Link group on both DeviceB and DeviceD, add interface 1 and interface 3 to the Monitor Link groups as uplink interfaces, and add interface 2 and interface 4 to the groups as downlink interfaces.
2. Configure a WTR time for the Monitor Link groups.


#### Procedure

1. Create Monitor Link groups and add uplink and downlink interfaces to each group.
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] monitor-link group 1 
   [*DeviceB-mtlk-group1] port 100ge 1/0/1 uplink
   [*DeviceB-mtlk-group1] port 100ge 1/0/2 downlink 1 
   [*DeviceB-mtlk-group1] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] monitor-link group 2 
   [*DeviceD-mtlk-group2] port 100ge 1/0/3 uplink 
   [*DeviceD-mtlk-group2] port 100ge 1/0/4 downlink 1 
   [~DeviceD-mtlk-group2] commit
   ```
2. Configure a WTR time for the Monitor Link groups.
   
   # Configure DeviceB.
   ```
   [~DeviceB-mtlk-group1] timer recover-time 10 
   [*DeviceB-mtlk-group1] commit 
   ```
   
   # Configure DeviceD.
   ```
   [~DeviceD-mtlk-group2] timer recover-time 10 
   [*DeviceD-mtlk-group2] commit 
   ```

#### Verifying the Configuration

* Run the [**display monitor-link group**](cmdqueryname=display+monitor-link+group) *group-id* command to check the Monitor Link group configuration.
  ```
  [~DeviceD] display monitor-link group 2 
   Monitor Link group 2 information :
     Status: Enable   
     Recover-timer: 10 second(s).  
     Remain-time: 0 second(s)                                                      
     Member                 Role         State Remain-time(s) Last-change-time                 
     100GE1/0/3             Uplink       UP    --       0000/00/00 00:00:00 UTC+05:00
     100GE1/0/4             Downlink[1]  UP    --       0000/00/00 00:00:00 UTC+05:00
  ```


#### Configuration Scripts

* DeviceB
  
  ```
  # 
  sysname DeviceB 
  #
  monitor-link group 1  
   port 100GE1/0/1 uplink  
   port 100GE1/0/2 downlink 1  
   timer recover-time 10 
  # 
  return
  ```
* DeviceD
  
  ```
  # 
  sysname DeviceD
  #
  monitor-link group 2  
   port 100GE1/0/3 uplink  
   port 100GE1/0/4 downlink 1  
   timer recover-time 10 
  # 
  return
  ```