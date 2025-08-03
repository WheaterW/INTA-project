Example for Configuring OSPF Virtual Links
==========================================

This section describes how to configure virtual links to connect a non-backbone area to the backbone area.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365649__fig_dc_vrp_ospf_cfg_205401), Area 2 is not directly connected to the backbone area Area 0. Area 1 serves as a transit area to connect Area 2 and Area 0. A virtual link is configured between DeviceA and DeviceB.

**Figure 1** Networking for configuring an OSPF virtual links![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_ospf_cfg_205401.png)  


#### Precautions

The default value is recommended when a virtual link is created. You can modify the value in actual scenarios.

Suggestions for configuring parameters are as follows:

* The smaller the [**hello**](cmdqueryname=hello) parameter, the more rapidly a Router detects network topology change, the more network resources are consumed.
* If the [**retransmit**](cmdqueryname=retransmit) parameter is set too small, LSAs may be retransmitted. Setting the parameter to a large value is recommended in a low-speed network.
* The authentication modes of a virtual link and the backbone area must be the same.
* To improve security, OSPF area authentication or interface authentication is recommended. For details, see "Improving OSPF Network Security". OSPF area authentication is used as an example. For details, see Example for Configuring Basic OSPF Functions.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic OSPF functions on each Router.
2. Configure a virtual link between DeviceA and DeviceB to connect a non-backbone area to the backbone area.

#### Data Preparation

To complete the configuration, you need the following data:

| Device Name | Router ID | Process ID | IP Address |
| --- | --- | --- | --- |
| DeviceA | 1.1.1.1 | 1 | Area 0: 10.0.0.0/8  Area 1: 192.168.1.0/24 |
| DeviceB | 2.2.2.2 | 1 | Area 1: 192.168.1.0/24  Area 2: 172.16.0.0/16 |
| DeviceC | 3.3.3.3 | 1 | Area 0: 10.0.0.0/8 |
| DeviceD | 4.4.4.4 | 1 | Area 2: 172.16.0.0/16 |



#### Procedure

1. Assign an IP address to each interface according to [Configuration Files](#EN-US_TASK_0172365649__section_dc_vrp_ospf_cfg_205406). For configuration details, see Configuration Files in this section.
2. Configure basic OSPF functions.
   
   
   
   [Configuring Basic OSPF Functions](dc_vrp_ospf_cfg_0003.html) shows how to configure basic OSPF functions. For configuration details, see Configuration Files in this section.
3. Check the OSPF routes on DeviceA
   
   
   ```
   [~DeviceA] display ospf routing
   ```
   ```
             OSPF Process 1 with Router ID 1.1.1.1
                      Routing Tables
   
    Routing for Network
    Destination        Cost       Type       NextHop         AdvRouter       Area
    10.0.0.0/8         1          Transit    10.1.1.1        3.3.3.3         0.0.0.0
    192.168.1.0/24     1          Transit    192.168.1.1     1.1.1.1         0.0.0.1
   
    Total Nets: 2
    Intra Area: 2  Inter Area: 0  ASE: 0  NSSA: 0    
   ```
   
   The routing table on Device A contains no route in Area 2 because Area 2 is not directly connected to Area 0.
4. Configure an OSPF virtual link.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] router id 1.1.1.1
   ```
   ```
   [~DeviceA] ospf 1
   ```
   ```
   [*DeviceA-ospf-1] area 1
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.1] vlink-peer 2.2.2.2
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.1] quit
   ```
   ```
   [*DeviceA-ospf-1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] router id 2.2.2.2
   ```
   ```
   [~DeviceB] ospf 1
   ```
   ```
   [*DeviceB-ospf-1] area 1
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.1] vlink-peer 1.1.1.1
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.1] quit
   ```
   ```
   [*DeviceB-ospf-1] quit
   ```
   ```
   [*DeviceB] commit
   ```
5. Verify the configuration.
   
   
   
   # Display the OSPF vlink on DeviceA.
   
   ```
   [~DeviceA] display ospf vlink
   ```
   ```
             OSPF Process 1 with Router ID 1.1.1.1
                     Virtual Links
    Virtual-link Neighbor-id  -> 2.2.2.2, Neighbor-State: Full
    Interface: 192.168.1.1 (GigabitEthernet0/1/0)
    Cost: 1  State: P-2-P  Type: Virtual
    Transit Area: 0.0.0.1
    Timers: Hello 10 , Dead 40 , Retransmit 5 , Transmit Delay 1
    GR State: Normal
   ```
   
   The preceding command output shows that the OSPF vlink neighbor status is "Full".
   
   # Display the OSPF routes on DeviceA.
   
   ```
   [~DeviceA] display ospf routing
   ```
   ```
             OSPF Process 1 with Router ID 1.1.1.1
                      Routing Tables
   
    Routing for Network
    Destination        Cost       Type       NextHop         AdvRouter       Area
    172.16.0.0/16      2          Inter-area 192.168.1.2     2.2.2.2         0.0.0.2
    10.0.0.0/8         1          Transit    10.1.1.1        1.1.1.1         0.0.0.0
    192.168.1.0/24     1          Transit    192.168.1.1     1.1.1.1         0.0.0.1
   
    Total Nets: 3
    Intra Area: 2  Inter Area: 1  ASE: 0  NSSA: 0    
   ```
   
   After the virtual link is configured, the routing table on DeviceA contains routes in Area 2.

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceA
  ```
  ```
  #
  ```
  ```
  router id 1.1.1.1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.1 255.0.0.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.0.0.0 0.255.255.255
  ```
  ```
   area 0.0.0.1
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
    vlink-peer 2.2.2.2
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceB configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceB
  ```
  ```
  #
  ```
  ```
  router id 2.2.2.2
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.16.1.1 255.255.0.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.1
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
    vlink-peer 1.1.1.1
  ```
  ```
   area 0.0.0.2
  ```
  ```
    network 172.16.0.0 0.0.255.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceC configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceC
  ```
  ```
  #
  ```
  ```
  router id 3.3.3.3
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.2 255.0.0.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.0.0.0 0.255.255.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceD configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceD
  ```
  ```
  #
  ```
  ```
  router id 4.4.4.4
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.16.1.2 255.255.0.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.2
  ```
  ```
    network 172.16.0.0 0.0.255.255
  ```
  ```
  #
  ```
  ```
  return
  ```