Example for Connecting LANs Through VCs
=======================================

This example shows how to configure two devices in different LANs to communicate through VCs.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172364119__fig_dc_vrp_fr_cfg_001001), Routers are connected to each other through POS sub-interfaces. The type of the interface on Device A is DCE, and the type of the interface on Device B is DTE.

**Figure 1** Networking for connecting LANs through VCs  
![](images/fig_dc_vrp_fr_cfg_001001.png)  

| Device Name | Interface | IP Address |
| --- | --- | --- |
| DeviceA | POS0/1/0.1 | 10.1.1.1/24 |
| DeviceB | POS0/1/0.1 | 10.1.1.2/24 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Set the link layer protocol to FR.
2. Configure interface type.
3. Configure a DLCI for each VC.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces
* DLCI on each interface

#### Procedure

1. Configure RouterDevice A.
   
   
   
   # Set the link layer protocol to FR and interface type to DCE.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] interface Pos0/1/0
   ```
   ```
   [~DeviceA-Pos0/1/0] link-protocol fr
   ```
   ```
   [*DeviceA-Pos0/1/0] fr interface-type dce
   ```
   ```
   [*DeviceA-Pos0/1/0] quit
   ```
   
   # Configure an IP address for the sub-interface and the local DLCI.
   
   ```
   [~DeviceA] interface Pos0/1/0.1 p2p
   ```
   ```
   [~DeviceA-Pos0/1/0.1] ip address 10.1.1.1 255.255.255.0
   ```
   ```
   [*DeviceA-Pos0/1/0.1] fr dlci 100
   ```
   ```
   [*DeviceA-fr-dlci-Pos0/1/0.1-100] quit
   ```
   ```
   [*DeviceA-Pos0/1/0.1] quit
   ```
   
   # Commit the configuration.
   
   ```
   [*DeviceA] commit
   ```
2. Configure RouterDevice B.
   
   
   
   # Set the link layer protocol to FR and interface type to DTE.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] interface Pos0/1/0
   ```
   ```
   [~DeviceB-Pos0/1/0] link-protocol fr
   ```
   ```
   [*DeviceB-Pos0/1/0] fr interface-type dte
   ```
   ```
   [*DeviceB-Pos0/1/0] quit
   ```
   
   # Configure an IP address for the sub-interface and the local DLCI.
   
   ```
   [~DeviceB] interface Pos0/1/0.1 p2p
   ```
   ```
   [~DeviceB-Pos0/1/0.1] ip address 10.1.1.2 255.255.255.0
   ```
   ```
   [*DeviceB-Pos0/1/0.1] fr dlci 100
   ```
   ```
   [*DeviceB-fr-dlci-Pos0/1/0.1-100] quit
   ```
   ```
   [*DeviceB-Pos0/1/0.1] quit
   ```
   
   # Commit the configuration.
   
   ```
   [*DeviceB] commit
   ```
3. Check the configurations.
   
   
   
   Run the [**display fr interface**](cmdqueryname=display+fr+interface) command on Device B to check the FR protocol status and interface information. The command output shows that the physical status and protocol status of the interface are both Up.
   
   ```
   <DeviceB> display fr interface pos0/1/0.1
   ```
   ```
   Pos0/1/0.1, DTE, physical up, protocol up
   ```
   
   Run the [**display fr pvc-info**](cmdqueryname=display+fr+pvc-info) command on Device B to check VC configurations and statistics.
   
   ```
   <DeviceB> display fr pvc-info interface pos0/1/0.1
   ```
   ```
   PVC statistics for interface Pos0/1/0.1 (DTE, PP)
    DLCI = 111, USAGE = LOCAL, Pos0/1/0.1
    create time = 2013/11/05 11:19:17, status = ACTIVE
    in BECN = 0, in FECN = 0
    in packets = 0, in bytes = 0
    out packets = 0, out bytes = 0
   
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface Pos0/1/0
   link-protocol fr
   undo shutdown       
   fr interface-type dce
  #               
  interface Pos0/1/0.1 p2p
   ip address 10.1.1.1 255.255.255.0
   fr dlci 100    
  #
  return
  
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  interface Pos0/1/0
   link-protocol fr
   undo shutdown
   fr interface-type dte       
  #               
  interface Pos0/1/0.1 p2p
   ip address 10.1.1.2 255.255.255.0
   fr dlci 100    
  #
  return
  
  ```