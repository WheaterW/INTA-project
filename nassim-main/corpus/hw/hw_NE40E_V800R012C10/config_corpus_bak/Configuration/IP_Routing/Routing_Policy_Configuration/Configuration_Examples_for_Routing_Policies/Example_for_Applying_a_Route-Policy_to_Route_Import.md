Example for Applying a Route-Policy to Route Import
===================================================

By applying route-policies, you can control the import of routes and set attributes for imported routes.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172366592__fig_dc_vrp_route-policy_cfg_003001), DeviceB exchanges routing information with DeviceA through OSPF and with DeviceC through IS-IS.

It is required that IS-IS routes be imported into OSPF on DeviceB and that a route-policy be used to set route attributes. Specifically, the cost of the route 172.16.1.0/24 is set to 100, and the tag of the route 172.16.2.0/24 is set to 20.

**Figure 1** Applying a route-policy to route import![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, and interface4 represent GE0/1/0, GE0/2/0, GE0/3/0, and GE0/1/1, respectively.


  
![](images/fig_dc_vrp_route-policy_cfg_003001.png)

#### Precautions

During the configuration, pay attention to the following points:

* When configuring an IP prefix list, specify a proper IP prefix range according to actual requirements.
* The name of a route-policy is case sensitive.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic IS-IS functions on DeviceB and DeviceC.
2. Configure OSPF on DeviceA and DeviceB, and import IS-IS routes into OSPF.
3. Configure a route-policy on DeviceB, apply the route-policy to route import from IS-IS to OSPF, and check routing information.

#### Data Preparation

To complete the configuration, you need the following data:

* Area IDs, IS-IS levels, and system IDs of DeviceB and DeviceC
* Area IDs (0, indicating the OSPF backbone area) of DeviceA and DeviceB
* ACL number, name of the IP prefix list, cost of the route 172.16.1.0/24, and tag of the route 172.16.2.0/24

#### Procedure

1. Configure IP addresses for interfaces. For detailed configurations, see Configuration Files.
2. Configure IS-IS.
   
   
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] isis 1
   ```
   ```
   [*DeviceC-isis-1] is-level level-2
   ```
   ```
   [*DeviceC-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*DeviceC-isis-1] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/1] isis enable 1
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceC] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] interface GigabitEthernet 0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceC] interface GigabitEthernet 0/3/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] isis enable 1
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/3/0] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] isis 1
   ```
   ```
   [*DeviceB-isis-1] is-level level-2
   ```
   ```
   [*DeviceB-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*DeviceB-isis-1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/2/0] quit
   ```
3. Configure OSPF and import routes.
   
   
   
   # Enable OSPF on DeviceA.
   
   ```
   [~DeviceA] ospf 1
   ```
   ```
   [*DeviceA-ospf-1] area 0
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceA-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~DeviceA-ospf-1] quit
   ```
   
   # Enable OSPF and import IS-IS routes on DeviceB.
   
   ```
   [~DeviceB] ospf 1
   ```
   ```
   [*DeviceB-ospf-1] area 0
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceB-ospf-1] import-route isis 1
   ```
   ```
   [*DeviceB-ospf-1] commit
   ```
   ```
   [~DeviceB-ospf-1] quit
   ```
   
   # Check the OSPF routing table on DeviceA. The command output shows the imported routes.
   
   ```
   [~DeviceA] display ospf routing
   
             OSPF Process 1 with Router ID 192.168.1.1
                      Routing Tables
   
    Routing for Network
    Destination        Cost  Type       NextHop         AdvRouter       Area
    192.168.1.0/24     1  Stub       192.168.1.1     192.168.1.1     0.0.0.0
   
    Routing for ASEs
    Destination        Cost      Type       Tag         NextHop         AdvRouter
    172.16.1.0/24      1        Type2      1           192.168.1.2     192.168.1.2
    172.16.2.0/24      1        Type2      1           192.168.1.2     192.168.1.2
    172.16.3.0/24      1        Type2      1           192.168.1.2     192.168.1.2
    192.168.2.0/24     1        Type2      1           192.168.1.2     192.168.1.2
   
    Routing for NSSAs
    Destination        Cost      Type       Tag         NextHop         AdvRouter
   
    Total Nets: 5
    Intra Area: 1  Inter Area: 0  ASE: 4  NSSA: 0
   
   ```
4. Configure filters.
   
   
   
   # Configure an ACL numbered **2002** to permit the route 172.16.2.0/24.
   
   ```
   [~DeviceB] acl number 2002
   ```
   ```
   [*DeviceB-acl4-basic-2002] rule permit source 172.16.2.0 0.0.0.255
   ```
   ```
   [*DeviceB-acl4-basic-2002] commit
   ```
   ```
   [~DeviceB-acl4-basic-2002] quit
   ```
   
   # Configure an IP prefix list named **prefix-a** to permit the route 172.16.1.0/24.
   
   ```
   [~DeviceB] ip ip-prefix prefix-a index 10 permit 172.16.1.0 24
   ```
   ```
   [*DeviceB] commit
   ```
5. Configure a route-policy.
   
   
   ```
   [~DeviceB] route-policy isis2ospf permit node 10
   ```
   ```
   [*DeviceB-route-policy] if-match ip-prefix prefix-a
   ```
   ```
   [*DeviceB-route-policy] apply cost 100
   ```
   ```
   [*DeviceB-route-policy] quit
   ```
   ```
   [*DeviceB] route-policy isis2ospf permit node 20
   ```
   ```
   [*DeviceB-route-policy] if-match acl 2002
   ```
   ```
   [*DeviceB-route-policy] apply tag 20
   ```
   ```
   [*DeviceB-route-policy] quit
   ```
   ```
   [*DeviceB] route-policy isis2ospf permit node 30
   ```
   ```
   [*DeviceB] commit
   ```
   ```
   [~DeviceB-route-policy] quit
   ```
6. Apply the route-policy to route import.
   
   
   
   # Apply the route-policy to route import on DeviceB.
   
   ```
   [~DeviceB] ospf
   ```
   ```
   [*DeviceB-ospf-1] import-route isis 1 route-policy isis2ospf
   ```
   ```
   [*DeviceB-ospf-1] commit
   ```
   ```
   [~DeviceB-ospf-1] quit
   ```
   
   # Check the OSPF routing table on DeviceA. The command output shows that the cost of the route 172.16.1.0/24 is 100, the tag of the route 172.16.2.0/24 is 20, and that attributes of other routes remain unchanged.
   
   ```
   [~DeviceA] display ospf routing
   
             OSPF Process 1 with Router ID 192.168.1.1
                      Routing Tables
    Routing for Network
    Destination        Cost  Type       NextHop         AdvRouter       Area
    192.168.1.0/24     1  Stub       192.168.1.1     192.168.1.1     0.0.0.0
   
    Routing for ASEs
    Destination        Cost      Type       Tag         NextHop         AdvRouter
    172.16.1.0/24      100       Type2      1           192.168.1.2     192.168.1.2
    172.16.2.0/24      1          Type2      20          192.168.1.2     192.168.1.2
    172.16.3.0/24      1          Type2      1           192.168.1.2     192.168.1.2
    192.168.2.0/24     1          Type2      1           192.168.1.2     192.168.1.2
   
    Routing for NSSAs
    Destination        Cost      Type       Tag         NextHop         AdvRouter
   
    Total Nets: 5
    Intra Area: 1  Inter Area: 0  ASE: 4  NSSA: 0
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
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 192.168.1.0 0.0.0.255
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
  acl number 2002
  ```
  ```
   rule 5 permit source 172.16.2.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   is-level level-2
  ```
  ```
   network-entity 10.0000.0000.0002.00
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
   ip address 192.168.2.2 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   import-route isis 1 route-policy isis2ospf
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  route-policy isis2ospf permit node 10
  ```
  ```
   if-match ip-prefix prefix-a
  ```
  ```
   apply cost 100
  ```
  ```
  #
  ```
  ```
  route-policy isis2ospf permit node 20
  ```
  ```
   if-match acl 2002
  ```
  ```
   apply tag 20
  ```
  ```
  #
  ```
  ```
  route-policy isis2ospf permit node 30
  ```
  ```
  #
  ```
  ```
  ip ip-prefix prefix-a index 10 permit 172.16.1.0 24
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
  isis 1
  ```
  ```
   is-level level-2
  ```
  ```
   network-entity 10.0000.0000.0001.00
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
   ip address 172.16.1.1 255.255.255.0
  ```
  ```
   isis enable 1
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
   ip address 172.16.2.1 255.255.255.0
  ```
  ```
   isis enable 1
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
   ip address 172.16.3.1 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.2.1 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  return
  ```