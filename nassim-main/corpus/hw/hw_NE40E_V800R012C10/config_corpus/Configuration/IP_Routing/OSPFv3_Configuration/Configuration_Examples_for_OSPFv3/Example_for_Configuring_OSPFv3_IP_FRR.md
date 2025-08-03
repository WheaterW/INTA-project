Example for Configuring OSPFv3 IP FRR
=====================================

This section describes the procedure for configuring OSPFv3 IP FRR, including how to block FRR on certain interfaces to prevent the links connected to these interfaces from functioning as backup links and how to bind OSPFv3 IP FRR to a BFD session.

#### Networking Requirements

When a fault occurs on the network, OSPFv3 IP FRR rapidly switches traffic to the backup link without waiting for route convergence. This ensures non-stop traffic forwarding.

As shown in [Figure 1](#EN-US_TASK_0172365806__fig_dc_vrp_ospfv3_cfg_206601):

* OSPFv3 runs on all devices.
* The link cost meets the OSPFv3 IP FRR traffic protection inequality.
* If the primary link T fails, it is required that the traffic from Device S be rapidly redirected to the backup link that passes through Device N.
* Based on the network planning, the link passing through Device A does not function as a backup link.

**Figure 1** Networking for configuring OSPFv3 IP FRR![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 4 in this example represent GE0/1/0, GE0/2/0, GE0/3/0, and GE0/1/1, respectively.


  
![](images/fig_dc_vrp_ospfv3_cfg_206601.png)

#### Precautions

When configuring OSPFv3 IP FRR, note the following points:

* Before configuring OSPFv3 IP FRR, block FRR on certain interfaces to prevent the links connected to these interfaces from functioning as backup links. After that, the link where the interface resides is not calculated as a backup link during FRR calculation.
* When OSPFv3 IP FRR is configured, the underlying layer must be able to quickly respond to link changes so that traffic can be quickly switched to the backup link. After the [**bfd all-interfaces**](cmdqueryname=bfd+all-interfaces) **frr-binding** command is run, the BFD session status is bound to the link status of the interface (when the BFD session goes down, the link status of the interface also goes down). In this manner, faults can be rapidly detected.
* To improve security, you are advised to deploy OSPFv3 authentication. For details, see "Configuring OSPFv3 Authentication". OSPFv3 IPsec is used as an example. For details, see "Example for Configuring IPsec for OSPFv3."

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic OSPFv3 functions on each Router. (For configuration details, see [Example for Configuring Basic OSPFv3 Functions](dc_vrp_ospfv3_cfg_2063.html).)
2. Configure BFD for OSPFv3 on all devices in Area 0.
3. Set the costs of links to ensure that link T is selected to transmit traffic.
4. Block FRR on the specified interface on Device S.
5. Enable OSPFv3 IP FRR on DeviceA to protect the traffic forwarded by DeviceA.


#### Data Preparation

To complete the configuration, you need the following data:

| Device | Router ID | Interface | IPv6 Address |
| --- | --- | --- | --- |
| Device S | 1.1.1.1 | GE0/1/0 | 2001:DB8:1000::1/96 |
| GE0/2/0 | 2001:DB8:1001::1/96 |
| GE0/3/0 | 2001:DB8:1002::1/96 |
| Device A | 2.2.2.2 | GE0/1/0 | 2001:DB8:1000::2/96 |
| GE0/2/0 | 2001:DB8:2000::2/96 |
| Device N | 3.3.3.3 | GE0/1/0 | 2001:DB8:1002::2/96 |
| GE0/2/0 | 2001:DB8:2002::2/96 |
| Device E | 4.4.4.4 | GE0/1/0 | 2001:DB8:2000::1/96 |
| GE0/2/0 | 2001:DB8:2001::1/96 |
| GE0/3/0 | 2001:DB8:2002::1/96 |
| GE0/1/1 | 2001:DB8:3000::1/96 |



#### Procedure

1. Assign an IPv6 address to each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172365806__section_dc_vrp_ospfv3_cfg_206606) in this section.
2. Configure basic OSPFv3 functions. See [Example for Configuring Basic OSPFv3 Functions](dc_vrp_ospfv3_cfg_2063.html).
3. Configure BFD for OSPFv3 on all devices in Area 0. See [Example for Configuring BFD for OSPFv3](dc_vrp_ospfv3_cfg_2069.html).
4. Set the costs of links to ensure that link T is selected to transmit traffic.
   
   
   
   # Configure Device S.
   
   ```
   [~DeviceS] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceS-GigabitEthernet0/1/0] ospfv3 cost 5
   ```
   ```
   [*DeviceS-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceS] interface gigabitethernet0/2/0
   ```
   ```
   [*DeviceS-GigabitEthernet0/2/0] ospfv3 cost 15
   ```
   ```
   [*DeviceS-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceS] interface gigabitethernet0/3/0
   ```
   ```
   [*DeviceS-GigabitEthernet0/3/0] ospfv3 cost 10
   ```
   ```
   [*DeviceS-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceS] commit
   ```
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] ospfv3 cost 5
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet0/2/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] ospfv3 cost 5
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   
   
   # Configure Device N.
   
   ```
   [~DeviceN] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceN-GigabitEthernet0/1/0] ospfv3 cost 10
   ```
   ```
   [*DeviceN-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceN] interface gigabitethernet0/2/0
   ```
   ```
   [*DeviceN-GigabitEthernet0/2/0] ospfv3 cost 10
   ```
   ```
   [*DeviceN-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceN] commit
   ```
5. Block FRR on the specified interface on Device S.
   
   
   ```
   [~DeviceS] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceS-GigabitEthernet0/1/0] ospfv3 frr block
   ```
   ```
   [*DeviceS-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceS] commit
   ```
6. Enable OSPFv3 IP FRR on Device S.
   
   
   ```
   [~DeviceS] ospfv3
   ```
   ```
   [*DeviceS-ospfv3-1] frr
   ```
   ```
   [*DeviceS-ospfv3-1-frr] loop-free-alternate
   ```
   ```
   [*DeviceS-ospfv3-1-frr] commit
   ```
7. Verify the configuration.
   
   
   
   # Run the **display ospfv3 routing** command on Device S to view routing information.
   
   ```
   [~DeviceS-ospfv3-1-frr] display ospfv3 routing 2001:db8:3000::1 96
   ```
   ```
    Codes : E2 - Type 2 External, E1 - Type 1 External, IA - Inter-Area,
            N - NSSA
    Flags: A - Added to URT6, LT - Locator Routing
   
    OSPFv3 Process (1)
      Destination                                Metric
        Nexthop
      2001:DB8:2000:1::/64                       3124
          via 2001:DB8:2001::1/96, GE0/2/0
             backup via FE80::2000:10FF:4, GE0/3/0, LFA LINK-NODE
        Priority      :Low
   ```
   
   The preceding command output shows that a backup link has been generated on DeviceS through FRR calculation.

#### Configuration Files

* Device S configuration file
  
  ```
  #
  sysname DeviceS
  #
   bfd
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:1000::1/96
   ospfv3 1 area 0.0.0.1
   ospfv3 cost 5
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:1001::1/96
   ospfv3 1 area 0.0.0.1
   ospfv3 cost 15
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:1002::1/96
   ospfv3 1 area 0.0.0.1
   ospfv3 frr block
   ospfv3 cost 10
  #
  ospfv3 1
   router-id 1.1.1.1
   bfd all-interfaces enable
   bfd all-interfaces frr-binding
   frr
    loop-free-alternate
   area 0.0.0.1
  #
  return
  ```
* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
   bfd
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:1000::2/96
   ospfv3 1 area 0.0.0.1
   ospfv3 cost 5
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:2000::2/96
   ospfv3 1 area 0.0.0.1
   ospfv3 cost 5
  #
  ospfv3 1
   router-id 2.2.2.2
   bfd all-interfaces enable
   bfd all-interfaces frr-binding
   frr
    loop-free-alternate
   area 0.0.0.1
  #
  return
  ```
* Device N configuration file
  
  ```
  #
  sysname DeviceN
  #
   bfd
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:1002::2/96
   ospfv3 1 area 0.0.0.1
   ospfv3 cost 10
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:2002::2/96
   ospfv3 1 area 0.0.0.1
   ospfv3 cost 10
  #
  ospfv3 1
   router-id 3.3.3.3
   bfd all-interfaces enable
   bfd all-interfaces frr-binding
   frr
   area 0.0.0.1
  #
  return
  ```
* Device E configuration file
  
  ```
  #
  sysname DeviceE
  #
   bfd
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:2000::1/96
   ospfv3 1 area 0.0.0.1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:2001::1/96
   ospfv3 1 area 0.0.0.1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:2002::1/96
   ospfv3 1 area 0.0.0.1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:3000::1/96
   ospfv3 1 area 0.0.0.1
   ospfv3 cost 5
  #
  ospfv3 1
   router-id 4.4.4.4
   bfd all-interfaces enable
   bfd all-interfaces frr-binding
   area 0.0.0.1
  #
  return
  ```