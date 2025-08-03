Example for Applying Route-Policies
===================================

By configuring route-policies, you can flexibly control the traffic on a complex network.

#### Networking Requirements

[Figure 1](#EN-US_TASK_0172366595__fig_dc_vrp_route-policy_cfg_003101) shows a simplified diagram of the MPLS network that carries multiple types of L3VPN services, such as multimedia, signaling, and accounting. In [Figure 1](#EN-US_TASK_0172366595__fig_dc_vrp_route-policy_cfg_003101), two sites, each of which has two PEs accessing the core layer, are used as an example. The core layer is divided into two planes, each of which has three fully meshed P nodes. Nodes in different planes are connected to provide backup paths. MP-BGP is used to advertise inner tags and VPNv4 routes between the PEs. Each PE needs to establish the MP-IBGP peer relationship with a route reflector (RR).

![](../../../../public_sys-resources/note_3.0-en-us.png) 

[Figure 1](#EN-US_TASK_0172366595__fig_dc_vrp_route-policy_cfg_003101) is a simplified networking diagram, in which there are two sites, one RR, and two planes with six P nodes. On the actual network, there are 14 sites with 28 PEs, and each plane has four P nodes and two RRs. Therefore, each RR needs to establish MP-IBGP connections with 28 PEs.


**Figure 1** Applying route-policies  
![](images/fig_dc_vrp_route-policy_cfg_003101.png)  

In [Figure 1](#EN-US_TASK_0172366595__fig_dc_vrp_route-policy_cfg_003101), each PE sends BGP Update messages to the RR, and the other PEs receive BGP Update messages from different planes. Therefore, route-policies need to be applied to ensure that a VPN traffic flow is transmitted through only one plane.


#### Precautions

When applying route-policies, note the following rules:

* Configure different route distinguishers (RDs) for the two PEs in the same site.
* Assign different community attributes for the routes advertised by PEs in different planes.
* Run the **undo policy vpn-target** command in the BGP-VPNv4 address family view to ensure that VPN-target-based filtering is not performed on VPNv4 routes.
* When applying a routing policy, ensure that the routing policy name is case sensitive.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure different RDs for two PEs in the same site to ensure that each PE can receive two routes from different BGP next hops in the remote site. When two PEs in a site advertise the routes to the same destination, configuring different RDs for the two PEs can ensure that BGP peers consider the advertised routes as two different routes. This is because BGP-VPNv4 uses the VPNv4 addresses that consist of IPv4 addresses and RDs.
2. Assign different community attributes to the routes advertised by the PE in plane A and the routes advertised by the PE in plane B.
3. Set different local priorities for routes based on the community attributes of the routes. In this manner, the PE in plane A preferentially selects the routes advertised by the remote PE in plane A, and the PE in plane B preferentially selects the routes advertised by the remote PE in plane B.

#### Data Preparation

To complete the configuration, you need the following data.

**Table 1** IP addresses of physical interfaces
| Local Device | Local Interface and Its IP Address | Remote Interface and Its IP Address | Remote Device |
| --- | --- | --- | --- |
| P1 | GE 0/1/0  10.1.1.1/30 | GE 0/1/0  10.1.1.2/30 | P3 |
| P1 | GE 0/2/0  10.1.2.1/30 | GE 0/1/0  10.1.2.2/30 | P5 |
| P1 | GE 0/3/0  10.1.3.1/30 | GE 0/1/0  10.1.3.2/30 | RR |
| P1 | GE 0/1/1  10.1.4.1/30 | GE 0/1/0  10.1.4.2/30 | P2 |
| P1 | GE 0/1/2  10.1.5.1/30 | GE 0/1/0  10.1.5.2/30 | PE1 |
| P2 | GE 0/1/1  10.1.6.1/30 | GE 0/1/0  10.1.6.2/30 | P6 |
| P2 | GE 0/3/0  10.1.7.1/30 | GE 0/1/0  10.1.7.2/30 | P4 |
| P2 | GE 0/2/0  10.1.8.1/30 | GE 0/2/0  10.1.8.2/30 | RR |
| P2 | GE 0/1/2  10.1.9.1/30 | GE 0/1/0  10.1.9.2/30 | PE2 |
| P3 | GE 0/2/0  10.1.10.1/30 | GE 0/2/0  10.1.10.2/30 | P5 |
| P3 | GE 0/3/0  10.1.11.1/30 | GE 0/2/0  10.1.11.2/30 | P4 |
| P3 | GE 0/1/1  10.1.12.1/30 | GE 0/1/0  10.1.12.2/30 | PE3 |
| P4 | GE 0/3/0  10.1.13.1/30 | GE 0/3/0  10.1.13.2/30 | P6 |
| P4 | GE 0/1/1  10.1.14.1/30 | GE 0/1/0  10.1.14.2/30 | PE4 |
| P5 | GE 0/3/0  10.1.15.1/30 | GE 0/2/0  10.1.15.2/30 | P6 |
| PE1 | GE 0/2/0  10.1.16.1/30 | GE 0/2/0  10.1.16.2/30 | PE2 |
| PE3 | GE 0/2/0  10.1.17.1/30 | GE 0/2/0  10.1.17.2/30 | PE4 |


**Table 2** IP addresses of loopback interfaces
| Local Device | IP Address of Local Loopback 0 Interface |
| --- | --- |
| P1 | 10.1.1.9/32 |
| P2 | 10.2.2.9/32 |
| P3 | 10.3.3.9/32 |
| P4 | 10.4.4.9/32 |
| P5 | 10.5.5.9/32 |
| P6 | 10.6.6.9/32 |
| PE1 | 10.7.7.9/32 |
| PE2 | 10.8.8.9/32 |
| PE3 | 10.9.9.9/32 |
| PE4 | 10.10.10.9/32 |
| RR | 10.11.11.9/32 |


**Table 3** BGP parameter values
| BGP Parameter | Value |
| --- | --- |
| AS number | 65000 |
| Router ID | Same as the address of Loopback 0 interface |
| BGP community attribute | Plane A: 65000:100  Plane B: 65000:200 |
| BGP local priority | Plane A: The local priority of community attribute 65000:100 is set to 200.  Plane B: The local priority of community attribute 65000:200 is set to 200. |
| Routing policy name | Policy to filter imported routes: **local\_pre**  Policy to filter routes to be advertised: **comm** |
| Community filter name | 1 |
| BGP peer group name | Client |



#### Procedure

1. Configure names for devices and IP addresses for interfaces.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172366595__section_dc_vrp_cfg_00652605) in this section.
2. Configure an IGP.
   
   
   
   In this example, IS-IS is used. For detailed configurations, see the configuration files in this example.
   
   After the configuration, run the **display ip routing-table** command. You can view that PEs, P nodes and PEs, and P nodes have learned the addresses of Loopback 0 interfaces from each other.
3. Establish MP-IBGP connections between PEs and RRs.
   
   
   
   # Use the configuration of PE1 as an example. Configurations of other PEs are similar to that of PE1. For configuration details, see [Configuration Files](#EN-US_TASK_0172366595__section_dc_vrp_cfg_00652605) in this section.
   
   ```
   [*PE1] bgp 65000
   [~PE1-bgp] peer 10.11.11.9 as-number 65000
   [*PE1-bgp] peer 10.11.11.9 connect-interface LoopBack0
   [*PE1-bgp] ipv4-family unicast
   [*PE1-bgp-af-ipv4] undo peer 10.11.11.9 enable
   [*PE1-bgp] ipv4-family vpnv4
   [*PE1-bgp-af-vpnv4] peer 10.11.11.9 enable
   [*PE1-bgp-af-vpnv4] commit
   ```
   
   # Configure the RR.
   
   ```
   [~RR] bgp 65000
   [*RR-bgp] group client internal
   [*RR-bgp] peer client connect-interface LoopBack0
   [*RR-bgp] ipv4-family unicast
   [*RR-bgp-af-ipv4] undo peer client enable
   [*RR-bgp-af-ipv4] quit
   [*RR-bgp] ipv4-family vpnv4
   [*RR-bgp-af-vpnv4] undo policy vpn-target
   [*RR-bgp-af-vpnv4] peer client enable
   [*RR-bgp-af-vpnv4] peer 10.7.7.9 group client
   [*RR-bgp-af-vpnv4] peer 10.8.8.9 group client
   [*RR-bgp-af-vpnv4] peer 10.9.9.9 group client
   [*RR-bgp-af-vpnv4] peer 10.10.10.9 group client
   [*RR-bgp-af-vpnv4] peer client reflect-client
   [*RR-bgp-af-vpnv4] commit
   [~RR-bgp-af-vpnv4] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The **undo policy vpn-target** command needs to be run in the BGP-VPNv4 address family view of the RR to ensure that VPN-target-based filtering is not performed on VPNv4 routes. By default, an RR performs VPN-target-based filtering on the received VPNv4 routes. The routes that match the filtering rules are added to the VPN routing table, and other routes are discarded. In this example, no VPN instances are configured on the RR. In this case, if VPN-target-based filtering is enabled, all the received VPNv4 routes will be discarded.
   
   After the configuration, run the **display bgp vpnv4 all peer** command on the RR. The following command output shows that the RR has established MP-IBGP connections with all PEs.
   
   ```
   <RR> display bgp vpnv4 all peer
    BGP local router ID : 10.11.11.9
    Local AS number : 65000
    Total number of peers : 4                 Peers in established state : 4
     Peer          V    AS     MsgRcvd  MsgSent  OutQ  Up/Down       State       PrefRcv
     10.7.7.9      4    65000  79       82        0     00:01:31     Established      0
     10.8.8.9      4    65000  42       66        0     00:01:16     Established      0
     10.9.9.9      4    65000  21       34        0     00:00:50     Established      0
     10.10.10.9    4    65000  2         4        0     00:00:21     Established      0
   
   ```
4. Configure route-policies.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Use the configurations of PE1, PE2, and the RR as an example. The configurations of PE3 and PE4 are similar to the configurations of PE1 and PE2 respectively. For configuration details, see [Configuration Files](#EN-US_TASK_0172366595__section_dc_vrp_cfg_00652605) in this section.
   
   # Configure a route-policy on PE1 so that the route advertised by the PE in plane A to the RR can carry community attribute 65000:100.
   
   ```
   [~PE1] route-policy comm permit node 10
   [*PE1-route-policy] apply community 65000:100
   [*PE1-route-policy] commit
   ```
   
   # Configure a route-policy on PE2 so that the route advertised by the PE in plane B to the RR can carry community attribute 65000:200.
   
   ```
   [~PE2] route-policy comm permit node 10
   [*PE2-route-policy] apply community 65000:200
   [*PE2-route-policy] commit
   ```
   
   # On PE1, apply the route-policy to the advertised BGP VPNv4 route so that the community attribute can be advertised to the RR.
   
   ```
   [~PE1] bgp 65000
   [*PE1-bgp] ipv4-family vpnv4
   [*PE1-bgp-af-vpnv4] peer 10.11.11.9 route-policy comm export
   [*PE1-bgp-af-vpnv4] peer 10.11.11.9 advertise-community
   [*PE1-bgp-af-vpnv4] commit
   ```
   
   # On PE2, apply the route-policy to the advertised BGP VPNv4 route so that the community attribute can be advertised to the RR.
   
   ```
   [~PE2] bgp 65000
   [*PE2-bgp] ipv4-family vpnv4
   [*PE2-bgp-af-vpnv4] peer 10.11.11.9 route-policy comm export
   [*PE2-bgp-af-vpnv4] peer 10.11.11.9 advertise-community
   [*PE2-bgp-af-vpnv4] commit
   ```
   
   # Configure the RR to advertise the community attributes to the PEs.
   
   ```
   [~RR] bgp 65000
   [*RR-bgp] ipv4-family vpnv4
   [*RR-bgp-af-vpnv4] peer client advertise-community
   [*RR-bgp-af-vpnv4] commit
   ```
   
   # Configure a community filter on PE1.
   
   ```
   [~PE1] ip community-filter 1 permit 65000:100
   [*PE1] commit
   ```
   
   # Configure a community filter on PE2.
   
   ```
   [~PE2] ip community-filter 1 permit 65000:200
   [*PE2] commit
   ```
   
   # On PE1, configure a route-policy and set the local preference of the route with community attribute 65000:100 to 200.
   
   ```
   [~PE1] route-policy local_pre permit node 10
   [*PE1-route-policy] if-match community-filter 1
   [*PE1-route-policy] apply local-preference 200
   [*PE1-route-policy] commit
   [~PE1-route-policy] quit
   ```
   
   # On PE2, configure a route-policy and set the local preference of the route with community attribute 65000:200 to 200.
   
   ```
   [~PE2] route-policy local_pre permit node 10
   [*PE2-route-policy] if-match community-filter 1
   [*PE2-route-policy] apply local-preference 200
   [*PE2-route-policy] commit
   [~PE2-route-policy] quit
   ```
   
   # On PE1, apply the route-policy to the imported BGP VPNv4 route so that the PE in plane A prefers the route advertised by the remote PE in plane A.
   
   ```
   [~PE1] bgp 65000
   [*PE1-bgp] ipv4-family vpnv4
   [*PE1-bgp-af-vpnv4] peer 10.11.11.9 route-policy local_pre import
   [*PE1-bgp-af-vpnv4] commit
   ```
   
   # On PE2, apply the route-policy to the imported BGP VPNv4 route so that the PE in plane B prefers the route advertised by the remote PE in plane B.
   
   ```
   [~PE2] bgp 65000
   [*PE2-bgp] ipv4-family vpnv4
   [*PE2-bgp-af-vpnv4] peer 10.11.11.9 route-policy local_pre import
   [*PE2-bgp-af-vpnv4] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After this configuration, you also need to configure MPLS, establish tunnels, configure MPLS L3VPN functions, and connect the PEs to CEs. For configuration details, see [Configuration Files](#EN-US_TASK_0172366595__section_dc_vrp_cfg_00652605) in this section.
5. Verify the configuration.
   
   
   
   # Run the **display bgp vpnv4 all routing-table community** command on a PE to view information about the VPNv4 routes with community attributes. Use the command output on PE1 and PE2 as an example.
   
   ```
   [~PE1] display bgp vpnv4 all routing-table community
   Total Number of Routes from all PE: 2
   BGP Local router ID is 10.7.7.9
   Status codes: * - valid, > - best, d - damped,
                 h - history,  i - internal, s - suppressed, S - Stale
                 Origin : i - IGP, e - EGP, ? - incomplete
   
   
    Route Distinguisher: 65000:10001012
          Network        NextHop        MED        LocPrf    PrefVal  Community
   *>   10.22.1.0/24     10.9.9.9         0           200             65000:100
   *                     10.10.10.9       0           100             65000:200
   
    Total routes of vpn-instance NGN_Media: 2
         Network         NextHop        MED        LocPrf    PrefVal  Community
    *>i  10.22.1.0/24    10.9.9.9         0           200       0     65000:100
   *                     10.10.10.9       0           100       0     65000:200
   
   [~PE2] display bgp vpnv4 all routing-table community
   Total Number of Routes from all PE: 2
   BGP Local router ID is 10.8.8.9
   Status codes: * - valid, > - best, d - damped,
                 h - history,  i - internal, s - suppressed, S - Stale
                 Origin : i - IGP, e - EGP, ? - incomplete
   
   
    Route Distinguisher: 65000:10001011
          Network        NextHop        MED        LocPrf    PrefVal  Community
   *>   10.22.1.0/24     10.10.10.9       0          200              65000:200
   *                     10.9.9.9         0          100              65000:100
   
    Total routes of vpn-instance NGN_Media: 2
         Network         NextHop        MED        LocPrf    PrefVal  Community
    *>i  10.22.1.0/24    10.10.10.9       0         200        0      65000:200
   *                     10.9.9.9         0         100        0      65000:100
   ```
   
   # Run the **display ip routing-table vpn-instance NGN\_Media 10.22.1.0 24** command on PE1. The command output shows that the next hop of the route to 10.22.1.0/24 is PE3, indicating that PE1 prefers the route advertised by PE3.
   
   ```
   [~PE1] display ip routing-table vpn-instance NGN_Media 10.22.1.0 24
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: NGN_Media
   Destination/Mask  Proto  Pre  Cost  Flags  NextHop   Interface
      10.22.1.0/24   BGP    255  0       RD   10.9.9.9  GigabitEthernet0/1/0
   ```

#### Configuration Files

* P1 configuration file
  
  ```
  #
  sysname P1
  #
  mpls lsr-id 10.1.1.9
  #
  mpls
  #
  mpls ldp
  #
  isis 64
   network-entity 49.0091.0100.0100.1009.00
  #
  interface GigabitEthernet0/1/0
   description toP3GE0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/2/0
   description toP5GE0/1/0
   undo shutdown
   ip address 10.1.2.1 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/3/0
   description toRRGE0/1/0
   undo shutdown
   ip address 10.1.3.1 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/1/1
   description toP2GE0/1/0
   undo shutdown
   ip address 10.1.4.1 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/1/2
   description toP2GE0/1/0
   undo shutdown
   ip address 10.1.5.1 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface LoopBack0
   ip address 10.1.1.9 255.255.255.255
   isis enable 64
  #
  return
  ```
* P2 configuration file
  
  ```
  #
  sysname P2
  #
  mpls lsr-id 10.2.2.9
  #
  mpls
  #
  mpls ldp
  #
  isis 64
   network-entity 49.0091.0100.0200.2009.00
  #
  interface GigabitEthernet0/1/0
   description toP1GE0/1/1
   undo shutdown
   ip address 10.1.4.2 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/2/0
   description toRRGE0/2/0
   undo shutdown
   ip address 10.1.8.1 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/3/0
   description toP4GE0/1/0
   undo shutdown
   ip address 10.1.7.1 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/1/1
   description toP6GE0/1/0
   undo shutdown
   ip address 10.1.6.1 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/1/2
   description toPE2GE0/1/0
   undo shutdown
   ip address 10.1.9.1 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface LoopBack0
   ip address 10.2.2.9 255.255.255.255
   isis enable 64
  #
  return
  ```
* P3 configuration file
  
  ```
  #
  sysname P3
  #
  mpls lsr-id 10.3.3.9
  #
  mpls
  #
  mpls ldp
  #
  isis 64
   network-entity 49.0091.0100.0300.3009.00
  #
  interface GigabitEthernet0/1/0
   description toP1GE0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/2/0
   description toP5GE0/2/0
   undo shutdown
   ip address 10.1.10.1 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/3/0
   description toP4GE0/2/0
   undo shutdown
   ip address 10.1.11.1 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/1/1
   description toPE3GE0/1/0
   undo shutdown
   ip address 10.1.12.1 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface LoopBack0
   ip address 10.3.3.9 255.255.255.255
   isis enable 64
  #
  return
  ```
* P4 configuration file
  
  ```
  #
  sysname P4
  #
  mpls lsr-id 10.4.4.9
  #
  mpls
  #
  mpls ldp
  #
  isis 64
   network-entity 49.0091.0100.0400.4009.00
  #
  interface GigabitEthernet0/1/0
   description toP2GE0/3/0
   undo shutdown
   ip address 10.1.7.2 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/2/0
   description toP3GE0/3/0
   undo shutdown
   ip address 10.1.11.2 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/3/0
   description toP6GE0/3/0
   undo shutdown
   ip address 10.1.13.1 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/1/1
   description toPE4GE0/1/0
   undo shutdown
   ip address 10.1.14.1 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface LoopBack0
   ip address 10.4.4.9 255.255.255.255
   isis enable 64
  #
  return
  ```
* P5 configuration file
  
  ```
  #
  sysname P5
  #
  mpls lsr-id 10.5.5.9
  #
  mpls
  #
  mpls ldp
  #
  isis 64
   network-entity 49.0091.0100.0500.5009.00
  #
  interface GigabitEthernet0/1/0
   description toP1GE0/2/0
   undo shutdown
   ip address 10.1.2.2 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/2/0
   description toP3GE0/2/0
   undo shutdown
   ip address 10.1.10.2 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/3/0
   description toP6GE0/2/0
   undo shutdown
   ip address 10.1.15.1 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface LoopBack0
   ip address 10.5.5.9 255.255.255.255
   isis enable 64
  #
  return
  ```
* P6 configuration file
  
  ```
  #
  sysname P6
  #
  mpls lsr-id 10.6.6.9
  #
  mpls
  #
  mpls ldp
  #
  isis 64
   network-entity 49.0091.0100.0600.6009.00
  #
  interface GigabitEthernet0/1/0
   description toP2GE0/1/1
   undo shutdown
   ip address 10.1.6.2 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/2/0
   description toP5GE0/3/0
   undo shutdown
   ip address 10.1.15.2 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/3/0
   description toP4GE0/3/0
   undo shutdown
   ip address 10.1.13.2 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface LoopBack0
   ip address 10.6.6.9 255.255.255.255
   isis enable 64
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance NGN_Media
   route-distinguisher 65000:10001012
   apply-label per-instance
   vpn-target 65000:100 export-extcommunity
   vpn-target 65000:100 import-extcommunity
   vpn-target 65000:200 import-extcommunity
   vpn-target 65000:300 import-extcommunity
  ip vpn-instance NGN_Other
   route-distinguisher 65000:30001012
   apply-label per-instance
   vpn-target 65000:300 export-extcommunity
   vpn-target 65000:100 import-extcommunity
   vpn-target 65000:200 import-extcommunity
   vpn-target 65000:300 import-extcommunity
  ip vpn-instance NGN_Signaling
   route-distinguisher 65000:20001012
   apply-label per-instance
   vpn-target 65000:200 export-extcommunity
   vpn-target 65000:100 import-extcommunity
   vpn-target 65000:200 import-extcommunity
   vpn-target 65000:300 import-extcommunity
  #
  mpls lsr-id 10.7.7.9
  #
  mpls
  #
  mpls ldp
  #
  isis 64
   network-entity 49.0091.0100.0700.7009.00
  #
  interface GigabitEthernet0/1/0
   description toP1GE0/1/2
   undo shutdown
   ip address 10.1.5.2 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/2/0
   description toPE2GE0/2/0
   undo shutdown
   ip address 10.1.16.1 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/3/0
   undo shutdown
  #
  interface GigabitEthernet0/3/0.10
   ip binding vpn-instance NGN_Media
   vlan-type dot1q 10
   ip address 10.21.1.73 255.255.255.252
  #
  interface GigabitEthernet0/3/0.11
   ip binding vpn-instance NGN_Signaling
   vlan-type dot1q 11
   ip address 10.21.1.77 255.255.255.252
  #
  interface GigabitEthernet0/3/0.12
   ip binding vpn-instance NGN_Other
   vlan-type dot1q 12
   ip address 10.21.1.81 255.255.255.252
  #
  interface LoopBack0
   ip address 10.7.7.9 255.255.255.255
   isis enable 64
  #
  bgp 65000
   peer 10.11.11.9 as-number 65000
   peer 10.11.11.9 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization 
    undo peer 10.11.11.9 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 10.11.11.9 enable
    peer 10.11.11.9 route-policy local_pre import
    peer 10.11.11.9 route-policy comm export
    peer 10.11.11.9 advertise-community
   #
   ipv4-family vpn-instance NGN_Media
    aggregate 10.21.1.0 255.255.255.0 detail-suppressed
    import-route direct
   #
   ipv4-family vpn-instance NGN_Other
    aggregate 10.21.1.0 255.255.255.0 detail-suppressed
    import-route direct
   #
   ipv4-family vpn-instance NGN_Signaling
    aggregate 10.21.1.0 255.255.255.0 detail-suppressed
    import-route direct
  #
  route-policy comm permit node 10
   apply community 65000:100
  #
  ip community-filter 1 permit 65000:100
  #
  route-policy local_pre permit node 10
   if-match community-filter 1
   apply local-preference 200
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  ip vpn-instance NGN_Media
   route-distinguisher 65000:10001011
   apply-label per-instance
   vpn-target 65000:100 export-extcommunity
   vpn-target 65000:100 import-extcommunity
   vpn-target 65000:200 import-extcommunity
   vpn-target 65000:300 import-extcommunity
  ip vpn-instance NGN_Other
   route-distinguisher 65000:30001011
   apply-label per-instance
   vpn-target 65000:300 export-extcommunity
   vpn-target 65000:100 import-extcommunity
   vpn-target 65000:200 import-extcommunity
   vpn-target 65000:300 import-extcommunity
  ip vpn-instance NGN_Signaling
   route-distinguisher 65000:20001011
   apply-label per-instance
   vpn-target 65000:200 export-extcommunity
   vpn-target 65000:100 import-extcommunity
   vpn-target 65000:200 import-extcommunity
   vpn-target 65000:300 import-extcommunity
  #
  mpls lsr-id 10.8.8.9
  #
  mpls
  #
  mpls ldp
  #
  isis 64
   network-entity 49.0091.0100.0800.8009.00
  #
  interface GigabitEthernet0/1/0
   description toP2GE0/1/2
   undo shutdown
   ip address 10.1.9.2 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/2/0
   description toPE1GE0/2/0
   undo shutdown
   ip address 10.1.16.2 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/3/0
   undo shutdown
  #
  interface GigabitEthernet0/3/0.10
   ip binding vpn-instance NGN_Media
   vlan-type dot1q 10
   ip address 10.21.1.13 255.255.255.252
  #
  interface GigabitEthernet0/3/0.11
   ip binding vpn-instance NGN_Signaling
   vlan-type dot1q 11
   ip address 10.21.1.17 255.255.255.252
  #
  interface GigabitEthernet0/3/0.12
   ip binding vpn-instance NGN_Other
   vlan-type dot1q 12
   ip address 10.21.1.21 255.255.255.252
  #
  interface LoopBack0
   ip address 10.8.8.9 255.255.255.255
   isis enable 64
  #
  bgp 65000
   peer 10.11.11.9 as-number 65000
   peer 10.11.11.9 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization 
    undo peer 10.11.11.9 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 10.11.11.9 enable
    peer 10.11.11.9 route-policy local_pre import
    peer 10.11.11.9 route-policy comm export
    peer 10.11.11.9 advertise-community
   #
   ipv4-family vpn-instance NGN_Media
    aggregate 10.21.1.0 255.255.255.0 detail-suppressed
    import-route direct
   #
   ipv4-family vpn-instance NGN_Other
    aggregate 10.21.1.0 255.255.255.0 detail-suppressed
    import-route direct
   #
   ipv4-family vpn-instance NGN_Signaling
    aggregate 10.21.1.0 255.255.255.0 detail-suppressed
    import-route direct
  #
  route-policy comm permit node 10
   apply community 65000:200
  #
  ip community-filter 1 permit 65000:200
  #
  route-policy local_pre permit node 10
   if-match community-filter 1
   apply local-preference 200
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  ip vpn-instance NGN_Media
   route-distinguisher 65000:10000811
   apply-label per-instance
   vpn-target 65000:100 export-extcommunity
   vpn-target 65000:100 import-extcommunity
   vpn-target 65000:200 import-extcommunity
   vpn-target 65000:300 import-extcommunity
  ip vpn-instance NGN_Other
   route-distinguisher 65000:30000811
   apply-label per-instance
   vpn-target 65000:300 export-extcommunity
   vpn-target 65000:100 import-extcommunity
   vpn-target 65000:200 import-extcommunity
   vpn-target 65000:300 import-extcommunity
  ip vpn-instance NGN_Signaling
   route-distinguisher 65000:20000811
   apply-label per-instance
   vpn-target 65000:200 export-extcommunity
   vpn-target 65000:100 import-extcommunity
   vpn-target 65000:200 import-extcommunity
   vpn-target 65000:300 import-extcommunity
  #
  mpls lsr-id 10.9.9.9
  #
  mpls
  #
  mpls ldp
  #
  isis 64
   network-entity 49.0091.0100.0900.9009.00
  #
  interface GigabitEthernet0/1/0
   description toP3GE0/1/1
   undo shutdown
   ip address 10.1.12.2 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/2/0
   description toPE4GE0/2/0
   undo shutdown
   ip address 10.1.17.1 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/3/0
   undo shutdown
  #
  interface GigabitEthernet0/3/0.10
   ip binding vpn-instance NGN_Media
   vlan-type dot1q 10
   ip address 10.22.1.73 255.255.255.252
  #
  interface GigabitEthernet0/3/0.11
   ip binding vpn-instance NGN_Signaling
   vlan-type dot1q 11
   ip address 10.22.1.77 255.255.255.252
  #
  interface GigabitEthernet0/3/0.12
   ip binding vpn-instance NGN_Other
   vlan-type dot1q 12
   ip address 10.22.1.81 255.255.255.252
  #
  interface LoopBack0
   ip address 10.9.9.9 255.255.255.255
   isis enable 64
  #
  bgp 65000
   peer 10.11.11.9 as-number 65000
   peer 10.11.11.9 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization 
    undo peer 10.11.11.9 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 10.11.11.9 enable
    peer 10.11.11.9 route-policy local_pre import
    peer 10.11.11.9 route-policy comm export
    peer 10.11.11.9 advertise-community
   #
   ipv4-family vpn-instance NGN_Media
    aggregate 10.22.1.0 255.255.255.0 detail-suppressed
    import-route direct
   #
   ipv4-family vpn-instance NGN_Other
    aggregate 10.22.1.0 255.255.255.0 detail-suppressed
    import-route direct
   #
   ipv4-family vpn-instance NGN_Signaling
    aggregate 10.22.1.0 255.255.255.0 detail-suppressed
    import-route direct
  #
  route-policy comm permit node 10
   apply community 65000:100
  #
  ip community-filter 1 permit 65000:100
  #
  route-policy local_pre permit node 10
   if-match community-filter 1
   apply local-preference 200
  #
  route-policy local_pre permit node 20
  #
  return
  ```
* PE4 configuration file
  
  ```
  #
  sysname PE4
  #
  ip vpn-instance NGN_Media
   route-distinguisher 65000:10000712
   apply-label per-instance
   vpn-target 65000:100 export-extcommunity
   vpn-target 65000:100 import-extcommunity
   vpn-target 65000:200 import-extcommunity
   vpn-target 65000:300 import-extcommunity
  #
  ip vpn-instance NGN_Other
   route-distinguisher 65000:30000712
   apply-label per-instance
   vpn-target 65000:300 export-extcommunity
   vpn-target 65000:100 import-extcommunity
   vpn-target 65000:200 import-extcommunity
   vpn-target 65000:300 import-extcommunity
  #
  ip vpn-instance NGN_Signaling
   route-distinguisher 65000:20000712
   apply-label per-instance
   vpn-target 65000:200 export-extcommunity
   vpn-target 65000:100 import-extcommunity
   vpn-target 65000:200 import-extcommunity
   vpn-target 65000:300 import-extcommunity
  #
  mpls lsr-id 10.10.10.9
  #
  mpls
  #
  mpls ldp
  #
  isis 64
   network-entity 49.0091.0100.1001.0009.00
  #
  interface GigabitEthernet0/1/0
   description toP4GE0/1/1
   undo shutdown
   ip address 10.1.14.2 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/2/0
   description toPE3GE0/2/0
   undo shutdown
   ip address 10.1.17.2 255.255.255.252
   mpls
   mpls ldp
   isis enable 64
  #
  interface GigabitEthernet0/3/0
   undo shutdown
  #
  interface GigabitEthernet0/3/0.10
   ip binding vpn-instance NGN_Media
   vlan-type dot1q 10
   ip address 10.22.1.13 255.255.255.252
  #
  interface GigabitEthernet0/3/0.11
   ip binding vpn-instance NGN_Signaling
   vlan-type dot1q 11
   ip address 10.22.1.17 255.255.255.252
  #
  interface GigabitEthernet0/3/0.12
   ip binding vpn-instance NGN_Other
   vlan-type dot1q 12
   ip address 10.22.1.21 255.255.255.252
  #
  interface LoopBack0
   ip address 10.10.10.9 255.255.255.255
   isis enable 64
  #
  bgp 65000
   peer 10.11.11.9 as-number 65000
   peer 10.11.11.9 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization 
    undo peer 10.11.11.9 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 10.11.11.9 enable
    peer 10.11.11.9 route-policy local_pre import
    peer 10.11.11.9 route-policy comm export
    peer 10.11.11.9 advertise-community
   #
   ipv4-family vpn-instance NGN_Media
    aggregate 10.22.1.0 255.255.255.0 detail-suppressed
    import-route direct
   #
   ipv4-family vpn-instance NGN_Other
    aggregate 10.22.1.0 255.255.255.0 detail-suppressed
    import-route direct
   #
   ipv4-family vpn-instance NGN_Signaling
    aggregate 10.22.1.0 255.255.255.0 detail-suppressed
    import-route direct
  #
  route-policy comm permit node 10
   apply community 65000:200
  #
  ip community-filter 1 permit 65000:200
  #
  route-policy local_pre permit node 10
   if-match community-filter 1
   apply local-preference 200
  #
  return
  ```
* RR configuration file
  
  ```
  #
  sysname RR
  #
  isis 64
   network-entity 49.0091.0100.1101.1009.00
  #
  interface GigabitEthernet0/1/0
   description toP1GE0/3/0
   undo shutdown
   ip address 10.1.3.2 255.255.255.252
   isis enable 64
  #
  interface GigabitEthernet0/2/0
   description toP2GE0/2/0
   undo shutdown
   ip address 10.1.8.2 255.255.255.252
   isis enable 64
  #
  interface LoopBack0
   ip address 10.11.11.9 255.255.255.255
   isis enable 64
  #
  bgp 65000
   group client internal
   peer client connect-interface LoopBack0
   peer 10.7.7.9 as-number 65000
   peer 10.8.8.9 as-number 65000
   peer 10.9.9.9 as-number 65000
   peer 10.10.10.9 as-number 65000
  #
   ipv4-family unicast
    undo synchronization 
    undo peer client enable
    undo peer 10.7.7.9 enable
    undo peer 10.8.8.9 enable
    undo peer 10.9.9.9 enable
    undo peer 10.10.10.9 enable
   #
   ipv4-family vpnv4
    undo policy vpn-target
    peer client enable
    peer client reflect-client
    peer client advertise-community
    peer 10.7.7.9 enable
    peer 10.7.7.9 group client
    peer 10.8.8.9 enable
    peer 10.8.8.9 group client
    peer 10.9.9.9 enable
    peer 10.9.9.9 group client
    peer 10.10.10.9 enable
    peer 10.10.10.9 group client
  #
  return
  ```