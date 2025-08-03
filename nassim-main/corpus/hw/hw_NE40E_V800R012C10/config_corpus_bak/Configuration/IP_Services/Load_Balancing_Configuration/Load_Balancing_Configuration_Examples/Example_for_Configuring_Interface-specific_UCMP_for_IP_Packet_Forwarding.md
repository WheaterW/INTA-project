Example for Configuring Interface-specific UCMP for IP Packet Forwarding
========================================================================

This section provides an example for configuring interface-specific UCMP for IP packet forwarding.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172365026__fig_dc_ne_loadba_cfg_200901), Device A and Device E are connected through three links that pass through Device B, Device C, and Device D, respectively. The bandwidth of the link from Device A to Device B is 1 Gbit/s, that from Device A to Device C is 1 Gbit/s, and that from Device A to Device D is 10 Gbit/s. To allow traffic to be load balanced among these paths, configure UCMP for IP packet forwarding. In this example, configure UCMP on specified interfaces, not on an entire Router.

**Figure 1** Configuring interface-specific UCMP  
![](images/fig_dc_ne_loadba_cfg_200901.png)

**Table 1** Device names, interface names, and IP addresses
| Device Name | Interface Name | IP Address |
| --- | --- | --- |
| Device A | GE0/3/1 | 10.30.1.1/24 |
| GE 0/3/0 | 10.40.1.1/24 |
| 10GE0/2/0 | 10.50.1.1/24 |
| Device B | GE 0/1/0 | 10.30.1.2/24 |
| GE 0/2/0 | 10.60.1.2/24 |
| Device C | GE 0/1/0 | 10.40.1.2/24 |
| GE 0/2/0 | 10.70.1.2/24 |
| Device D | 10GE0/1/0 | 10.50.1.2/24 |
| GE 0/2/0 | 10.80.1.2/24 |
| Device E | GE0/3/1 | 10.60.1.1/24 |
| GE 0/3/0 | 10.70.1.1/24 |
| GE 0/2/0 | 10.80.1.1/24 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IGP on each Router. IS-IS is used in this example.
2. Enable UCMP on each interface, allowing three paths between Device A and Device E to perform UCMP during IP packet forwarding.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

For security purposes, you are advised not to use weak security algorithms in the IS-IS feature. If you need to use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function first.



#### Data Preparation

To complete the configuration, you need the following data:

* Type and number of each interface
* IP address of each interface
* IS-IS area ID and level for each Router

#### Procedure

1. Assign an IP address to each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172365026__example1916532552214034) in this section.
2. Configure basic IS-IS functions.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] isis 1
   ```
   ```
   [*DeviceA-isis-1] is-level level-1
   ```
   ```
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*DeviceA-isis-1] commit
   ```
   ```
   [~DeviceA-isis-1] quit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface 10gigabitethernet 0/2/0
   ```
   ```
   [*DeviceA-10GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*DeviceA-10GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/3/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/1] isis enable 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/0] isis enable 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] isis 1
   ```
   ```
   [*DeviceB-isis-1] is-level level-1
   ```
   ```
   [*DeviceB-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*DeviceB-isis-1] commit
   ```
   ```
   [~DeviceB-isis-1] quit
   ```
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] isis 1
   ```
   ```
   [*DeviceC-isis-1] is-level level-1
   ```
   ```
   [*DeviceC-isis-1] network-entity 10.0000.0000.0003.00
   ```
   ```
   [*DeviceC-isis-1] commit
   ```
   ```
   [~DeviceC-isis-1] quit
   ```
   ```
   [~DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure Device D.
   
   ```
   [~DeviceD] isis 1
   ```
   ```
   [*DeviceD-isis-1] is-level level-1
   ```
   ```
   [*DeviceD-isis-1] network-entity 10.0000.0000.0004.00
   ```
   ```
   [*DeviceD-isis-1] commit
   ```
   ```
   [~DeviceD-isis-1] quit
   ```
   ```
   [~DeviceD] interface 10gigabitethernet 0/1/0
   ```
   ```
   [~DeviceD-10GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceD-10GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceD] commit
   ```
   
   # Configure Device E.
   
   ```
   [~DeviceE] isis 1
   ```
   ```
   [*DeviceE-isis-1] is-level level-1
   ```
   ```
   [*DeviceE-isis-1] network-entity 10.0000.0000.0005.00
   ```
   ```
   [*DeviceE-isis-1] commit
   ```
   ```
   [~DeviceE-isis-1] quit
   ```
   ```
   [~DeviceE] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceE-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceE-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceE] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceE-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*DeviceE-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceE] interface gigabitethernet 0/3/1
   ```
   ```
   [*DeviceE-GigabitEthernet0/3/1] isis enable 1
   ```
   ```
   [*DeviceE-GigabitEthernet0/3/1] quit
   ```
   ```
   [*DeviceE] interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceE-GigabitEthernet0/3/0] isis enable 1
   ```
   ```
   [*DeviceE-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceE] commit
   ```
3. Enable UCMP on every outbound interface of Device A.
   
   
   ```
   [~DeviceA] interface 10gigabitethernet 0/2/0
   [~DeviceA-10GigabitEthernet0/2/0] undo shutdown
   [~DeviceA-10GigabitEthernet0/2/0] load-balance unequal-cost enable
   [*DeviceA-10GigabitEthernet0/2/0] quit
   [*DeviceA] interface gigabitethernet 0/3/1
   [*DeviceA-GigabitEthernet0/3/1] undo shutdown
   [*DeviceA-GigabitEthernet0/3/1] load-balance unequal-cost enable
   [*DeviceA-GigabitEthernet0/3/1] quit
   [*RouterA] interface gigabitethernet 0/3/0
   [*DeviceA-GigabitEthernet0/3/0] undo shutdown
   [*RouterA-GigabitEthernet0/3/0] load-balance unequal-cost enable
   [*RouterA-GigabitEthernet0/3/0] quit
   [*RouterA] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The traffic tester measures the traffic bandwidth values on GE 0/3/1 (10.30.1.1/24), GE 0/3/0 (10.40.1.1/24), and 10GE 0/2/0 (10.50.1.1/24) of Device A and obtains the traffic ratio of 1:1:10.

#### Configuration Files

* Device A configuration file
  
  ```
  #
   sysname RouterA
  #
  isis 1
   is-level level-1
   network-entity 10.0000.0000.0001.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   isis enable 1
  #
  interface 10GigabitEthernet0/2/0
   undo shutdown
   load-balance unequal-cost enable
   ip address 10.50.1.1 255.255.255.0
   isis enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   load-balance unequal-cost enable
   ip address 10.40.1.1 255.255.255.0
   isis enable 1
  #
  interface GigabitEthernet0/3/1
  undo shutdown
   load-balance unequal-cost enable
   ip address 10.30.1.1 255.255.255.0
   isis enable 1
  #
  return
  
  ```
* Device B configuration file
  
  ```
  #
   sysname RouterB
  #
  isis 1
   is-level level-1
   network-entity 10.0000.0000.0002.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.30.1.2 255.255.255.0
   isis enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.60.1.2 255.255.255.0
   isis enable 1
  #
  return
  
  ```
* Device C configuration file
  
  ```
  #
   sysname RouterC
  #
  isis 1
  is-level level-1
   network-entity 10.0000.0000.0003.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.40.1.2 255.255.255.0
   isis enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.70.1.2 255.255.255.0
   isis enable 1
  #
  return
  
  ```
* Device D configuration file
  
  ```
  #
   sysname RouterD
  #
  isis 1
   is-level level-1
   network-entity 10.0000.0000.0004.00
  #
  interface 10GigabitEthernet0/1/0
   undo shutdown
   ip address 10.50.1.2 255.255.255.0
   isis enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.80.1.2 255.255.255.0
   isis enable 1
  #
  return
  
  ```
* Device E configuration file
  
  ```
  #
   sysname RouterE
  #
  isis 1
   is-level level-1
   network-entity 10.0000.0000.0005.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.20.1.1 255.255.255.0
   isis enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.80.1.1 255.255.255.0
   isis enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.70.1.1 255.255.255.0
   isis enable 1
  #
  interface GigabitEthernet0/3/1
   undo shutdown
   ip address 10.60.1.1 255.255.255.0
   isis enable 1
  #
  return
  
  ```