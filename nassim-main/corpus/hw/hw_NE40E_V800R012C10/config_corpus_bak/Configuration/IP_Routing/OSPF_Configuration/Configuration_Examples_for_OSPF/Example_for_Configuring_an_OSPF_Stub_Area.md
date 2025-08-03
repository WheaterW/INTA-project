Example for Configuring an OSPF Stub Area
=========================================

This section describes how to configure a stub area that imports static routes. Such configuration can reduce the number of LSAs advertised to this area without affecting route reachability.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365652__fig_dc_vrp_ospf_cfg_009501), all Routers run OSPF, and the entire AS is divided into three areas. DeviceA and DeviceB function as ABRs to advertise inter-area routes; DeviceD functions as the ASBR and imports external routes (static routes).

Configure Area 1 as a stub area to reduce the LSAs advertised to this area without affecting route reachability.

**Figure 1** Networking for configuring an OSPF stub area![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](images/fig_dc_vrp_ospf_cfg_009501.png)  


#### Precautions

When configuring an OSPF stub area, note the following rules:

* The backbone area cannot be configured as a stub area.
* An ASBR cannot exist in a stub area. That is, AS-external routes are not flooded in the stub area.
* A virtual link cannot pass through a stub area.
* To improve security, OSPF area authentication or interface authentication is recommended. For details, see "Improving OSPF Network Security". OSPF area authentication is used as an example. For details, see Example for Configuring Basic OSPF Functions.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic OSPF functions on each Router for interconnection.
2. Configure a static route on DeviceD and import it into OSPF.
3. Configure Area 1 as a stub area by running the [**stub**](cmdqueryname=stub) command on all Routers in Area 1 and check the OSPF routing information on DeviceC.
4. Prevent DeviceA from advertising Type 3 LSAs to the stub area, and check the OSPF routing information on DeviceC.

#### Data Preparation

To complete the configuration, you need the following data:

| Device Name | Router ID | Process ID | IP Address |
| --- | --- | --- | --- |
| DeviceA | 1.1.1.1 | 1 | Area 0: 192.168.0.0/24  Area 1: 192.168.1.0/24 |
| DeviceB | 2.2.2.2 | 1 | Area 0: 192.168.0.0/24  Area 2: 192.168.2.0/24 |
| DeviceC | 3.3.3.3 | 1 | Area 1: 192.168.1.0/24 and 172.16.1.0/24 |
| DeviceD | 4.4.4.4 | 1 | Area 2: 192.168.2.0/24 and 172.17.1.0/24 |
| DeviceE | 5.5.5.5 | 1 | Area 1: 172.16.1.0/24 |
| DeviceF | 6.6.6.6 | 1 | Area 2: 172.17.1.0/24 |



#### Procedure

1. Assign an IP address to each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172365652__section_dc_vrp_ospf_cfg_009506) in this section.
2. Configure basic OSPF functions. For details, see [Example for Configuring Basic OSPF Functions](dc_vrp_ospf_cfg_0094.html).
3. Configure DeviceD to import static routes.
   
   
   ```
   [*DeviceD] ip route-static 10.0.0.0 8 null 0
   ```
   ```
   [*DeviceD] ospf 1
   ```
   ```
   [*DeviceD-ospf-1] import-route static type 1
   ```
   ```
   [*DeviceD-ospf-1] commit
   ```
   ```
   [~DeviceD-ospf-1] quit
   ```
   
   # Display the ABR and ASBR information on DeviceC.
   
   ```
   [~DeviceC] display ospf abr-asbr
   
             OSPF Process 1 with Router ID 3.3.3.3
                     Routing Table to ABR and ASBR
   
    Type        Destination       Area       Cost  NextHop         RtType
    Intra-area  1.1.1.1           0.0.0.1    1     192.168.1.1     ABR
    Inter-area  4.4.4.4           0.0.0.1    3     192.168.1.1     ASBR
   ```
   
   # Display the OSPF routing table on DeviceC.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the area where DeviceC resides is a common area, external routes exist in the routing table.
   
   ```
   [~DeviceC] display ospf routing
   ```
   ```
             OSPF Process 1 with Router ID 3.3.3.3
                      Routing Tables
   
    Routing for Network
    Destination        Cost       Type       NextHop         AdvRouter       Area
   
    172.17.1.0/24      4          Inter-area 192.168.1.1     1.1.1.1         0.0.0.1
    192.168.0.0/24     2          Inter-area 192.168.1.1     1.1.1.1         0.0.0.1
    192.168.2.0/24     3          Inter-area 192.168.1.1     1.1.1.1         0.0.0.1
   
    Routing for ASEs
    Destination        Cost       Type       Tag        NextHop         AdvRouter
   
    10.0.0.0/8        4         Type1      1         192.168.1.1     4.4.4.4
   
   
    Total Nets: 4
    Intra Area: 0  Inter Area: 3  ASE: 1  NSSA: 0
   ```
4. Configure Area 1 as a stub area.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospf 1
   ```
   ```
   [*DeviceA-ospf-1] area 1
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.1] stub
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.1] commit
   ```
   ```
   [~DeviceA-ospf-1-area-0.0.0.1] quit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ospf 1
   ```
   ```
   [*DeviceC-ospf-1] area 1
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.1] stub
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.1] commit
   ```
   ```
   [~DeviceC-ospf-1-area-0.0.0.1] quit
   ```
   
   # Configure DeviceE.
   
   ```
   [~DeviceE] ospf 1
   ```
   ```
   [*DeviceE-ospf-1] area 1
   ```
   ```
   [*DeviceE-ospf-1-area-0.0.0.1] stub
   ```
   ```
   [*DeviceE-ospf-1-area-0.0.0.1] commit
   ```
   ```
   [~DeviceE-ospf-1-area-0.0.0.1] quit
   ```
   
   # Display the routing table on DeviceC.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the area where DeviceC resides is configured as a stub area, a default route rather than AS external routes is displayed in the routing table.
   
   ```
   [~DeviceC] display ospf routing
   ```
   ```
             OSPF Process 1 with Router ID 3.3.3.3
                      Routing Tables
   
    Routing for Network
    Destination        Cost       Type       NextHop         AdvRouter       Area
    0.0.0.0/0          2          Inter-area 192.168.1.1     1.1.1.1         0.0.0.1
    172.17.1.0/24      4          Inter-area 192.168.1.1     1.1.1.1         0.0.0.1
    192.168.0.0/24     2          Inter-area 192.168.1.1     1.1.1.1         0.0.0.1
    192.168.2.0/24     3          Inter-area 192.168.1.1     1.1.1.1         0.0.0.1
   
    Total Nets: 4
    Intra Area: 0  Inter Area: 4  ASE: 0  NSSA: 0
   ```
5. # Prevent DeviceA from advertising Type 3 LSAs to the stub area.
   
   
   ```
   [~DeviceA] ospf
   ```
   ```
   [*DeviceA-ospf-1] area 1
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.1] stub no-summary
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.1] commit
   ```
   ```
   [~DeviceA-ospf-1-area-0.0.0.1] quit
   ```
6. Verify the configuration.
   
   
   
   # Display the OSPF routing table on DeviceC.
   
   ```
   [~DeviceC] display ospf routing
   ```
   ```
             OSPF Process 1 with Router ID 3.3.3.3
                      Routing Tables
   
    Routing for Network
    Destination        Cost       Type       NextHop         AdvRouter       Area
    0.0.0.0/0          2          Inter-area 192.168.1.1     1.1.1.1         0.0.0.1
   
    Total Nets: 1
    Intra Area: 0  Inter Area: 1  ASE: 0  NSSA: 0
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the advertisement of summary LSAs to the stub area is disabled, the number of routing entries on the Routers in the stub area further decreases, and only the default route to a destination beyond the stub area is reserved.

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
   ip address 192.168.0.1 255.255.255.0
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
   ip address 192.168.1.1 255.255.255.0
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
    network 192.168.0.0 0.0.0.255
  ```
  ```
   area 0.0.0.1
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
    stub no-summary
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
  ip address 192.168.0.2 255.255.255.0
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
   ip address 192.168.2.1 255.255.255.0
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
    network 192.168.0.0 0.0.0.255
  ```
  ```
   area 0.0.0.2
  ```
  ```
    network 192.168.2.0 0.0.0.255
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
   ip address 172.16.1.1 255.255.255.0
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
    network 172.16.1.0 0.0.0.255
  ```
  ```
    stub
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown 
  ```
  ```
   ip address 192.168.2.2 255.255.255.0
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
   ip address 172.17.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   import-route static type 1
  ```
  ```
   area 0.0.0.2
  ```
  ```
    network 192.168.2.0 0.0.0.255
  ```
  ```
    network 172.17.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  ip route-static 10.0.0.0 255.0.0.0 NULL0
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceE configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceE
  ```
  ```
  #
  ```
  ```
  router id 5.5.5.5
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
   ip address 172.16.1.2 255.255.255.0
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
    network 172.16.1.0 0.0.0.255
  ```
  ```
    stub
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceF configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceF
  ```
  ```
  #
  ```
  ```
  router id 6.6.6.6
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
   ip address 172.17.1.2 255.255.255.0
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
    network 172.17.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```