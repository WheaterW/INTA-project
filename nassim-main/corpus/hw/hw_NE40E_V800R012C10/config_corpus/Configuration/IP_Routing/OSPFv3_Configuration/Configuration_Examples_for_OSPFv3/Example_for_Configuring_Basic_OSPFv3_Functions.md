Example for Configuring Basic OSPFv3 Functions
==============================================

This section describes how to configure basic OSPFv3 functions, including enabling OSPF on each router and specifying network segments in different areas.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365800__fig_dc_vrp_ospfv3_cfg_206301), all Routers run OSPFv3. The entire AS is divided into three areas. DeviceB and DeviceC serve as ABRs to forward inter-area routes.

After the configuration is complete, each router should learn the routes to all network segments in the AS.

**Figure 1** Networking for configuring OSPFv3 areas![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](images/fig_dc_vrp_ospfv3_cfg_206301.png)  


#### Configuration Notes

When configuring basic OSPFv3 functions, note the following rules:

* The backbone area is responsible for forwarding inter-area routes. In addition, the routing information between non-backbone areas must be forwarded through the backbone area. OSPFv3 defines the following rules for the backbone area:
  
  + Connectivity must be available between non-backbone areas and the backbone area.
  + Connectivity must be available over the backbone area.
* The intervals at which Hello, Dead, and Poll packets are sent on the local interface must be the same as those on the remote interface. Otherwise, the OSPFv3 neighbor relationship cannot be established.
* To improve security, you are advised to deploy OSPFv3 authentication. For details, see "Configuring OSPFv3 Authentication." OSPFv3 IPSec is used as an example. For details, see "Example for Configuring IPSec for OSPFv3".

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable basic OSPFv3 functions on each Router.
2. Specify network segments in different areas.

#### Data Preparation

To complete the configuration, you need the following data:

| Device Name | Router ID | Process ID | IPv6 Address |
| --- | --- | --- | --- |
| Device A | 1.1.1.1 | 1 | Area 1: 2001:DB8:4::1/64 and 2001:DB8:2::2/64 |
| Device B | 2.2.2.2 | 1 | Area 0: 2001:DB8:1::1/64  Area 1: 2001:DB8:2::1/64 |
| Device C | 3.3.3.3 | 1 | Area 0: 2001:DB8:1::2/64  Area 2: 2001:DB8:3::1/64 |
| Device D | 4.4.4.4 | 1 | Area 2: 2001:DB8:3::2/64 |



#### Procedure

1. Assign an IPv6 address to each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172365800__section_dc_vrp_ospfv3_cfg_206306) in this section.
2. Configure basic OSPFv3 functions.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospfv3
   ```
   ```
   [*DeviceA-ospfv3-1] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-ospfv3-1] area 0.0.0.1
   ```
   ```
   [*DeviceA-ospfv3-1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet0/3/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/0] ospfv3 1 area 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet0/2/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] ospfv3 1 area 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ospfv3
   ```
   ```
   [*DeviceB-ospfv3-1] router-id 2.2.2.2
   ```
   ```
   [*DeviceB-ospfv3-1] area 0.0.0.0
   ```
   ```
   [*DeviceB-ospfv3-1] area 0.0.0.1
   ```
   ```
   [*DeviceB-ospfv3-1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ospfv3 1 area 0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet0/2/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] ospfv3 1 area 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ospfv3
   ```
   ```
   [*DeviceC-ospfv3-1] router-id 3.3.3.3
   ```
   ```
   [*DeviceC-ospfv3-1] area 0.0.0.0
   ```
   ```
   [*DeviceC-ospfv3-1] area 0.0.0.2
   ```
   ```
   [*DeviceC-ospfv3-1] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] ospfv3 1 area 0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ospfv3 1 area 2
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] ospfv3
   ```
   ```
   [*DeviceD-ospfv3-1] router-id 4.4.4.4
   ```
   ```
   [*DeviceD-ospfv3-1] area 0.0.0.2
   ```
   ```
   [*DeviceD-ospfv3-1] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] ospfv3 1 area 2
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceD] commit
   ```
3. Verify the configuration. 
   
   
   
   # Display the OSPFv3 neighbors of DeviceB. The state Full indicates that a neighbor relationship is established.
   
   ```
   [*DeviceB] display ospfv3 peer
   ```
   ```
      OSPFv3 Process (1)
      Total number of peer(s): 2
       Peer(s) in full state: 2
      OSPFv3 Area (0.0.0.1)
      Neighbor ID    Pri   State       Dead Time   Interface               Instance ID
      1.1.1.1        1     Full/ -     00:00:34    GigabitEthernet0/2/0    0
   
      OSPFv3 Area (0.0.0.0)
      Neighbor ID    Pri   State       Dead Time   Interface               Instance ID
      3.3.3.3        1     Full/ -     00:00:32    GigabitEthernet0/1/0    0
   ```
   
   # Display the OSPFv3 neighbors of DeviceC.
   
   ```
   [*DeviceC] display ospfv3 peer
   ```
   ```
      OSPFv3 Process (1)
      Total number of peer(s): 2
       Peer(s) in full state: 2
      OSPFv3 Area (0.0.0.0)
      Neighbor ID    Pri   State       Dead Time   Interface                Instance ID
      2.2.2.2        1     Full/ -     00:00:37    GigabitEthernet0/1/0     0
   
      OSPFv3 Area (0.0.0.2)
      Neighbor ID    Pri   State       Dead Time   Interface                Instance ID
      4.4.4.4        1     Full/ -     00:00:33    GigabitEthernet0/2/0     0
   ```
   
   # Display the OSPFv3 routing table of DeviceD.
   
   ```
   [~DeviceD] display ospfv3 routing
   ```
   ```
   Codes : E2 - Type 2 External, E1 - Type 1 External, IA - Inter-Area,
           N - NSSA  
   Flags: A - Added to URT6, LT - Locator Routing 
   
   OSPFv3 Process (1)
      Destination                                   Metric
        Next-hop
     IA 2001:DB8:1::/64                                     2
              via FE80::1572:0:5EF4:1, GigabitEthernet0/2/0
     IA 2001:DB8:2::/64                                     3
              via FE80::1572:0:5EF4:1, GigabitEthernet0/2/0
        2001:DB8:3::/64                                     1
              directly-connected, GigabitEthernet0/2/0
     IA 2001:DB8:4::/64                                     4
              via FE80::1572:0:5EF4:1, GigabitEthernet0/2/0
   ```

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
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:2::2/64
  ```
  ```
   ospfv3 1 area 0.0.0.1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:4::1/64
  ```
  ```
   ospfv3 1 area 0.0.0.1
  ```
  ```
  #
  ```
  ```
  ospfv3 1
  ```
  ```
   router-id 1.1.1.1
  ```
  ```
   area 0.0.0.1
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:1::1/64
  ```
  ```
   ospfv3 1 area 0.0.0.0
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:2::1/64
  ```
  ```
   ospfv3 1 area 0.0.0.1
  ```
  ```
  #
  ```
  ```
  ospfv3 1
  ```
  ```
   router-id 2.2.2.2
  ```
  ```
   area 0.0.0.0
  ```
  ```
   area 0.0.0.1
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:1::2/64
  ```
  ```
   ospfv3 1 area 0.0.0.0
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:3::1/64
  ```
  ```
   ospfv3 1 area 0.0.0.2
  ```
  ```
  #
  ```
  ```
  ospfv3 1
  ```
  ```
   router-id 3.3.3.3
  ```
  ```
   area 0.0.0.0
  ```
  ```
   area 0.0.0.2
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
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:3::2/64
  ```
  ```
   ospfv3 1 area 0.0.0.2
  ```
  ```
  #
  ```
  ```
  ospfv3 1
  ```
  ```
   router-id 4.4.4.4
  ```
  ```
   area 0.0.0.2
  ```
  ```
  #
  ```
  ```
  return
  ```