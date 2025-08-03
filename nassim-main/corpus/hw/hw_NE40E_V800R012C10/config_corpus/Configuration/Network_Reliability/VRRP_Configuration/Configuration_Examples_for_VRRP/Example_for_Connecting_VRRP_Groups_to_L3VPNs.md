Example for Connecting VRRP Groups to L3VPNs
============================================

In this example, a VRRP group is specified as a gateway connected to CEs in each Layer 3 virtual private network (L3VPN). This configuration allows various VRRP groups to load-balance traffic and hosts at different sites in each VPN to communicate with each other.

#### Networking Requirements

IT technologies, such as enterprise resource planning, Voice over Internet Protocol (VoIP), video conferencing, and online training, provide a framework for office automation and information access in enterprises. As network economy develops, enterprises have growing networks and partners, and employees are often on business trips. A carrier network is required to help an enterprise connect its headquarters and branches and provide convenient access services for the staff on business trips. The VPN technology was developed and used over an IP network to meet this requirement.

To improve VPN reliability, add VPN interfaces to different VRRP groups.

As shown in [Figure 1](#EN-US_TASK_0172361799__fig_dc_vrp_vrrp_cfg_012301), VPN-RED and VPN-BLUE are deployed and MPLS and VRRP are configured.

**Table 1** Networking diagram for connecting VRRP groups to an L3VPN
| Item | Networking Requirements |
| --- | --- |
| Backup groups | * PE-A and PE-B form backup groups 1 and 2. In backup group 1, PE-A functions as the master device and PE-B functions as the backup device. In backup group 2, PE-A functions as the backup device and PE-B functions as the master device. * CE-A uses the virtual IP address of backup group 1 as the default gateway address. * CE-B uses the virtual IP address of backup group 2 as the default gateway address. |
| VPN instances to which CEs belong | * CE-A and CE-D belong to the VPN-BLUE instance. * CE-B and CE-C belong to the VPN-RED instance. |
| VPN instances to which interfaces on PEs belong | * On PE-A, GE 0/1/0 belongs to the VPN-BLUE instance, and GE 0/2/0 belongs to the VPN-RED instance. * On PE-B, GE 0/1/0 belongs to the VPN-BLUE instance, and GE 0/2/0 belongs to the VPN-RED instance. * On PE-C, GE 0/1/0 belongs to the VPN-RED instance, and GE 0/2/0 belongs to the VPN-BLUE instance. |
| Routing protocol and MPLS | * OSPF is configured and MPLS is enabled on a public network. * Default routes are configured on CE-A and CE-B. CE-A and CE-B exchange VPN routing information with PE-A and PE-B, respectively. * BGP peer relationships are set up between PE-A and PE-B, between PE-A and PE-C, and between PE-B and PE-C to transmit VPN routing information. |


**Figure 1** Connecting VRRP groups to L3VPNs![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](images/fig_dc_vrp_vrrp_cfg_012301.png "Click to enlarge")  

| **Device** Name | **Interface** Name | IP Address and Mask | Instance to Which the Interface Belongs |
| --- | --- | --- | --- |
| P | GE0/1/0 | 192.168.1.2/24 | - |
| GE0/2/0 | 192.168.2.2/24 | - |
| GE0/3/0 | 192.168.3.2/24 | - |
| Loopback1 | 4.4.4.4/32 | - |
| PE-A | GE0/1/0 | 10.1.1.1/24 | VPN-BLUE |
| GE0/2/0 | 10.3.1.1/24 | VPN-RED |
| GE0/3/0 | 192.168.1.1/24 | - |
| Loopback1 | 1.1.1.1/32 | - |
| PE-B | GE0/1/0 | 10.1.1.2/24 | VPN-BLUE |
| GE0/2/0 | 10.3.1.2/24 | VPN-RED |
| GE0/3/0 | 192.168.2.1/24 | - |
| Loopback1 | 2.2.2.2/32 | - |
| PE-C | GE0/1/0 | 10.4.1.1/24 | VPN-RED |
| GE0/2/0 | 10.2.1.1/24 | VPN-BLUE |
| GE0/3/0 | 192.168.3.1/24 | - |
| Loopback1 | 3.3.3.3/32 | - |
| CE-A | GE0/1/0 | 10.1.1.100/24 | - |
| CE-B | GE0/1/0 | 10.3.1.100/24 | - |
| CE-C | GE0/1/0 | 10.4.1.100/24 | - |
| CE-D | GE0/1/0 | 10.2.1.100/24 | - |



#### Precautions

To complete the configuration, you need to perform the following operations:

1. Configure OSPF on each PE and P to ensure that the backbone network is reachable.
2. Enable MPLS and MPLS LDP, and set up LDP LSPs on the MPLS backbone network.
3. Configure VPN instances on each PE and connect each CE to a PE.
4. Set up an MP-IBGP peer relationship between PEs.
5. Configure a route on CE-A and CE-B.

For configuration details about Steps 1 through 5, see the chapter "BGP/MPLS IP VPN Configuration" in *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - VPN* or [Configuration Files](#EN-US_TASK_0172361799__example1223748637214023) in this section.

To improve security, you are advised to configure a VRRP security policy. For details, see "Example for Configuring a VRRP Group."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure backup groups 1 and 2 on PE-A and PE-B.
2. Configure PE-A as the master device and PE-B as the backup device in backup group 1.
3. Configure PE-A as the backup device and PE-B as the master device in backup group 2.

#### Data Preparation

To complete the configuration, you need the following data:

* ID and virtual IP address of each VRRP group
* Priority of each Router in each VRRP group

#### Procedure

1. Configure multi-instance VRRP on PE-A and PE-B.
   
   
   
   # Create backup group 1 on PE-A and set the priority of PE-A to 120 in backup group 1.
   
   ```
   <PE-A> system-view
   ```
   ```
   [~PE-A] interface gigabitethernet 0/1/0
   ```
   ```
   [~PE-A-GigabitEthernet0/1/0] vrrp vrid 1 virtual-ip 10.1.1.111
   ```
   ```
   [*PE-A-GigabitEthernet0/1/0] vrrp vrid 1 priority 120
   ```
   ```
   [*PE-A-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE-A-GigabitEthernet0/1/0] quit
   ```
   
   # Create backup group 2 on PE-A and retain the default priority for PE-A in backup group 2.
   
   ```
   [~PE-A] interface gigabitethernet 0/2/0
   ```
   ```
   [~PE-A-GigabitEthernet0/2/0] vrrp vrid 2 virtual-ip 10.3.1.111
   ```
   ```
   [*PE-A-GigabitEthernet0/2/0] commit
   ```
   ```
   [~PE-A-GigabitEthernet0/2/0] quit
   ```
   
   # Create backup group 1 on PE-B and retain the default priority (100) for PE-B in backup group 1.
   
   ```
   <PE-B> system-view
   ```
   ```
   [~PE-B] interface gigabitethernet 0/1/0
   ```
   ```
   [~PE-B-GigabitEthernet0/1/0] vrrp vrid 1 virtual-ip 10.1.1.111
   ```
   ```
   [*PE-B-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE-B-GigabitEthernet0/1/0] quit
   ```
   
   # Create backup group 2 on PE-B and set the priority of PE-B to 120 in backup group 2.
   
   ```
   [~PE-B] interface gigabitethernet 0/2/0
   ```
   ```
   [~PE-B-GigabitEthernet0/2/0] vrrp vrid 2 virtual-ip 10.3.1.111
   ```
   ```
   [*PE-B-GigabitEthernet0/2/0] vrrp vrid 2 priority 120
   ```
   ```
   [*PE-B-GigabitEthernet0/2/0] commit
   ```
   ```
   [~PE-B-GigabitEthernet0/2/0] quit
   ```
2. Verify the configuration.
   
   
   
   Run the **display ip routing-table vpn-instance** *vpn-instance-name* command on PE-A and PE-B. The command output shows that a route destined for the virtual IP address exists only in the routing table of PE-A.
   
   The following example uses the command output on PE-A.
   
   ```
   <PE-A> display ip routing-table vpn-instance VPN-BLUE
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : VPN-BLUE
            Destinations : 8       Routes : 8        
   
   Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface
   
          10.1.1.0/24  Direct 0    0             D  10.1.1.2        GigabitEthernet0/1/0
          10.1.1.1/32  Direct 0    0             D  10.1.1.1        GigabitEthernet0/1/0
        10.1.1.111/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
        10.1.1.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
         127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   
   Run the **ping** command supporting multi-VRRP on PE-A and PE-B.
   
   ```
   <PE-A> ping -vpn-instance VPN-BLUE 10.1.1.111
   ```
   ```
     PING 10.1.1.111: 56  data bytes, press CTRL_C to break
       Reply from 10.1.1.111: bytes=56 Sequence=1 ttl=255 time=50 ms
       Reply from 10.1.1.111: bytes=56 Sequence=2 ttl=255 time=60 ms
       Reply from 10.1.1.111: bytes=56 Sequence=3 ttl=255 time=60 ms
       Reply from 10.1.1.111: bytes=56 Sequence=4 ttl=255 time=40 ms
       Reply from 10.1.1.111: bytes=56 Sequence=5 ttl=255 time=60 ms
   
     --- 10.1.1.111 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 40/54/60 ms  
   ```
   
   The command output shows that the virtual IP address 10.1.1.111 can be pinged.

#### Configuration Files

* PE-A configuration file
  
  ```
  #
  ```
  ```
  sysname PE-A
  ```
  ```
  #
  ```
  ```
  ip vpn-instance VPN-BLUE
  ```
  ```
   ipv4-family
   route-distinguisher 100:1
  ```
  ```
   apply-label per-instance
  ```
  ```
   vpn-target 100:1 export-extcommunity
  ```
  ```
   vpn-target 100:1 import-extcommunity
  ```
  ```
  #
  ```
  ```
  ip vpn-instance VPN-RED
  ```
  ```
   ipv4-family
   route-distinguisher 200:1
  ```
  ```
   apply-label per-instance
  ```
  ```
   vpn-target 200:1 export-extcommunity
  ```
  ```
   vpn-target 200:1 import-extcommunity
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 1.1.1.1
  ```
  ```
  mpls
  ```
  ```
  #
  ```
  ```
  mpls ldp
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
   ip binding vpn-instance VPN-BLUE
  ```
  ```
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
   vrrp vrid 1 virtual-ip 10.1.1.111
  ```
  ```
   vrrp vrid 1 priority 120
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
   ip binding vpn-instance VPN-RED
  ```
  ```
   ip address 10.3.1.1 255.255.255.0
  ```
  ```
   vrrp vrid 2 virtual-ip 10.3.1.111
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
   ip address 192.168.1.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 1.1.1.1 255.255.255.255
  ```
  ```
  #
  ```
  ```
  bgp 100
  ```
  ```
   peer 3.3.3.3 as-number 100
  ```
  ```
   peer 3.3.3.3 connect-interface LoopBack1
  ```
  ```
  #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization
  ```
  ```
    peer 3.3.3.3 enable
  ```
  ```
  #
  ```
  ```
  ipv4-family vpnv4
  ```
  ```
    policy vpn-target
  ```
  ```
    peer 3.3.3.3 enable
  ```
  ```
   #
  ```
  ```
  ipv4-family vpn-instance VPN-BLUE
  ```
  ```
    import-route direct
  ```
  ```
   #
  ```
  ```
   ipv4-family vpn-instance VPN-RED
  ```
  ```
    import-route direct
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
    network 1.1.1.1 0.0.0.0
  ```
  ```
  return
  ```
* PE-B configuration file
  
  ```
  #
  ```
  ```
  sysname PE-B
  ```
  ```
  #
  ```
  ```
  ip vpn-instance VPN-BLUE
  ```
  ```
   ipv4-family
   route-distinguisher 100:1
  ```
  ```
   apply-label per-instance
  ```
  ```
   vpn-target 100:1 export-extcommunity
  ```
  ```
   vpn-target 100:1 import-extcommunity
  ```
  ```
  #
  ```
  ```
  ip vpn-instance VPN-RED
  ```
  ```
   ipv4-family
   route-distinguisher 200:1
  ```
  ```
   apply-label per-instance
  ```
  ```
   vpn-target 200:1 export-extcommunity
  ```
  ```
   vpn-target 200:1 import-extcommunity
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 2.2.2.2
  ```
  ```
  mpls
  ```
  ```
  #
  ```
  ```
  mpls ldp
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
   ip binding vpn-instance VPN-BLUE
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
   vrrp vrid 1 virtual-ip 10.1.1.111
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
   ip binding vpn-instance VPN-RED
  ```
  ```
   ip address 10.3.1.2 255.255.255.0
  ```
  ```
   vrrp vrid 2 virtual-ip 10.3.1.111
  ```
  ```
   vrrp vrid 2 priority 120
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
   ip address 192.168.2.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
    ip address 2.2.2.2 255.255.255.255
  ```
  ```
  #
  ```
  ```
  bgp 100
  ```
  ```
   peer 3.3.3.3 as-number 100
  ```
  ```
   peer 3.3.3.3 connect-interface LoopBack1
  ```
  ```
  #
  ```
  ```
  ipv4-family unicast
  ```
  ```
    undo synchronization
  ```
  ```
    peer 3.3.3.3 enable
  ```
  ```
  #
  ```
  ```
  ipv4-family vpnv4
  ```
  ```
    policy vpn-target
  ```
  ```
    peer 3.3.3.3 enable
  ```
  ```
  #
  ```
  ```
  ipv4-family vpn-instance VPN-BLUE
  ```
  ```
  import-route direct
  ```
  ```
  #
  ```
  ```
   ipv4-family vpn-instance VPN-RED
  ```
  ```
   import-route direct
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
    network 192.168.2.0 0.0.0.255
  ```
  ```
    network 2.2.2.2 0.0.0.0
  ```
  ```
  #
  return
  ```