Example for Configuring Intra-AS Seamless MPLS
==============================================

When the access, aggregation, and core layers belong to the same AS, intra-AS seamless MPLS can be configured to implement the service connectivity between base stations and an MME or SGW.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172368682__fig_dc_vrp_seamless_mpls_cfg_003102), the access, aggregation, and core layers belong to the same AS. Base stations need to communicate with an MME or SGW through a VPN. To meet this requirement, intra-AS seamless MPLS can be configured.

**Figure 1** Intra-AS seamless MPLS networking (1)  
![](images/fig_dc_vrp_seamless_mpls_cfg_003102.png)

Addresses of interfaces are planned for CSGs, AGGs, core ABRs, and MASGs shown in [Figure 2](#EN-US_TASK_0172368682__fig_dc_vrp_seamless_mpls_cfg_003101).

**Figure 2** Intra-AS seamless MPLS networking (2)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example are GE0/1/0 and GE0/2/0, respectively.


  
![](images/fig_dc_vrp_seamless_mpls_cfg_003101.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IGP protocols at the access, aggregation, and core layers to implement network connectivity at each layer.
2. Configure MPLS and MPLS LDP and establish MPLS LSPs on devices.
3. Establish IBGP peer relationships at each layer and enable devices to exchange labeled routes.
4. Configure each AGG and core ABR as RRs to help a CSG and MASG obtain the route destined for each other's loopback interface.
5. Configure a routing policy to control label distribution for a BGP LSP to be established on each device. The egress of the BGP LSP to be established needs to assign an MPLS label to the route advertised to an upstream node. If a transit node receives a labeled IPv4 route from downstream, the downstream node must re-assign an MPLS label to the transit node.

#### Data Preparation

To complete the configuration, you need the following data:

* OSPF process ID (1) at the access layer, IS-IS process ID (1) at the aggregation layer, and OSPF process ID (2) at the core layer
* MPLS LSR IDs: 1.1.1.1 for the CSG, 2.2.2.2 for the AGG, 3.3.3.3 for the core ABR, and 4.4.4.4 for the MASG
* Name of a routing policy (policy1)

#### Procedure

1. Assign an IP address to each interface.
   
   
   
   Configure interface IP addresses and masks; configure a loopback interface address as an LSR ID on every device shown in [Figure 2](#EN-US_TASK_0172368682__fig_dc_vrp_seamless_mpls_cfg_003101); configure OSPF and IS-IS to advertise the route to the network segment of each interface and a host route to each loopback interface address (LSR ID). For configuration details, see Configuration Files in this section.
2. Enable MPLS and LDP globally on each device.
   
   
   
   # Configure the CSG.
   
   ```
   [~CSG] mpls lsr-id 1.1.1.1
   ```
   ```
   [*CSG] mpls
   ```
   ```
   [*CSG-mpls] quit
   ```
   ```
   [*CSG] mpls ldp
   ```
   ```
   [*CSG-mpls-ldp] quit
   ```
   ```
   [*CSG] interface GigabitEthernet 0/1/0
   ```
   ```
   [*CSG-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*CSG-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*CSG-GigabitEthernet0/1/0] quit
   ```
   ```
   [*CSG] commit
   ```
   
   # Configure the AGG.
   
   ```
   [~AGG] mpls lsr-id 2.2.2.2
   ```
   ```
   [*AGG] mpls
   ```
   ```
   [*AGG-mpls] quit
   ```
   ```
   [*AGG] mpls ldp
   ```
   ```
   [*AGG-mpls-ldp] quit
   ```
   ```
   [*AGG] interface GigabitEthernet 0/1/0
   ```
   ```
   [*AGG-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*AGG-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*AGG-GigabitEthernet0/1/0] quit
   ```
   ```
   [*AGG] interface GigabitEthernet 0/2/0
   ```
   ```
   [*AGG-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*AGG-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*AGG-GigabitEthernet0/2/0] quit
   ```
   ```
   [*AGG] commit
   ```
   
   # Configure the core ABR.
   
   ```
   [~Core ABR] mpls lsr-id 3.3.3.3
   ```
   ```
   [*Core ABR] mpls
   ```
   ```
   [*Core ABR-mpls] quit
   ```
   ```
   [*Core ABR] mpls ldp
   ```
   ```
   [*Core ABR-mpls-ldp] quit
   ```
   ```
   [*Core ABR] interface GigabitEthernet 0/1/0
   ```
   ```
   [*Core ABR-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*Core ABR-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*Core ABR-GigabitEthernet0/1/0] quit
   ```
   ```
   [*Core ABR] interface GigabitEthernet 0/2/0
   ```
   ```
   [*Core ABR-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*Core ABR-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*Core ABR-GigabitEthernet0/2/0] quit
   ```
   ```
   [*Core ABR] commit
   ```
   
   # Configure the MASG.
   
   ```
   [~MASG] mpls lsr-id 4.4.4.4
   ```
   ```
   [*MASG] mpls
   ```
   ```
   [*MASG-mpls] quit
   ```
   ```
   [*MASG] mpls ldp
   ```
   ```
   [*MASG-mpls-ldp] quit
   ```
   ```
   [*MASG] interface GigabitEthernet 0/1/0
   ```
   ```
   [*MASG-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*MASG-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*MASG-GigabitEthernet0/1/0] quit
   ```
   ```
   [*MASG] commit
   ```
3. Establish IBGP peer relationships at each layer and enable devices to exchange labeled routes.
   
   
   
   # Configure the CSG.
   
   ```
   [~CSG] bgp 100
   ```
   ```
   [*CSG-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*CSG-bgp] peer 2.2.2.2 connect-interface LoopBack 1
   ```
   ```
   [*CSG-bgp] peer 2.2.2.2 label-route-capability
   ```
   ```
   [*CSG-bgp] network 1.1.1.1 32
   ```
   ```
   [*CSG-bgp] quit
   ```
   ```
   [*CSG] commit
   ```
   
   # Configure the AGG.
   
   ```
   [~AGG] bgp 100
   ```
   ```
   [*AGG-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*AGG-bgp] peer 1.1.1.1 connect-interface LoopBack 1
   ```
   ```
   [*AGG-bgp] peer 1.1.1.1 label-route-capability
   ```
   ```
   [*AGG-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*AGG-bgp] peer 3.3.3.3 connect-interface LoopBack 1
   ```
   ```
   [*AGG-bgp] peer 3.3.3.3 label-route-capability
   ```
   ```
   [*AGG-bgp] quit
   ```
   ```
   [*AGG] commit
   ```
   
   # Configure the core ABR.
   
   ```
   [~Core ABR] bgp 100
   ```
   ```
   [*Core ABR-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*Core ABR-bgp] peer 2.2.2.2 connect-interface LoopBack 1
   ```
   ```
   [*Core ABR-bgp] peer 2.2.2.2 label-route-capability
   ```
   ```
   [*Core ABR-bgp] peer 4.4.4.4 as-number 100
   ```
   ```
   [*Core ABR-bgp] peer 4.4.4.4 connect-interface LoopBack 1
   ```
   ```
   [*Core ABR-bgp] peer 4.4.4.4 label-route-capability
   ```
   ```
   [*Core ABR-bgp] quit
   ```
   ```
   [*Core ABR] commit
   ```
   
   # Configure the MASG.
   
   ```
   [~MASG] bgp 100
   ```
   ```
   [*MASG-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*MASG-bgp] peer 3.3.3.3 connect-interface LoopBack 1
   ```
   ```
   [*MASG-bgp] peer 3.3.3.3 label-route-capability
   ```
   ```
   [*MASG-bgp] network 4.4.4.4 32
   ```
   ```
   [*MASG-bgp] quit
   ```
   ```
   [*MASG] commit
   ```
4. Configure each AGG and core ABR as RRs to help a CSG and MASG obtain the route destined for each other's loopback interface.
   
   
   
   # Configure the AGG.
   
   ```
   [~AGG] bgp 100
   ```
   ```
   [~AGG-bgp] peer 1.1.1.1 reflect-client
   ```
   ```
   [*AGG-bgp] peer 1.1.1.1 next-hop-local
   ```
   ```
   [*AGG-bgp] peer 3.3.3.3 reflect-client
   ```
   ```
   [*AGG-bgp] peer 3.3.3.3 next-hop-local
   ```
   ```
   [*AGG-bgp] quit
   ```
   ```
   [*AGG] commit
   ```
   
   # Configure the core ABR.
   
   ```
   [~Core ABR] bgp 100
   ```
   ```
   [~Core ABR-bgp] peer 2.2.2.2 reflect-client
   ```
   ```
   [*Core ABR-bgp] peer 2.2.2.2 next-hop-local
   ```
   ```
   [*Core ABR-bgp] peer 4.4.4.4 reflect-client
   ```
   ```
   [*Core ABR-bgp] peer 4.4.4.4 next-hop-local
   ```
   ```
   [*Core ABR-bgp] quit
   ```
   ```
   [*Core ABR] commit
   ```
5. Configure a routing policy on each device to establish a BGP LSP.
   
   
   
   # Configure a routing policy for advertising routes matching Route-Policy conditions to the CSG's BGP peer.
   
   ```
   [~CSG] route-policy policy1 permit node 1
   ```
   ```
   [*CSG-route-policy] apply mpls-label
   ```
   ```
   [*CSG-route-policy] quit
   ```
   ```
   [*CSG] bgp 100
   ```
   ```
   [*CSG-bgp] peer 2.2.2.2 route-policy policy1 export
   ```
   ```
   [*CSG-bgp] quit
   ```
   ```
   [*CSG] commit
   ```
   ```
   [~CSG] quit
   ```
   
   Repeat this step for the MASG. For configuration details, see Configuration Files in this section.
   
   # Configure a routing policy for advertising routes matching Route-Policy conditions to the AGG's BGP peer.
   
   ```
   [~AGG] route-policy policy1 permit node 1
   ```
   ```
   [*AGG-route-policy] if-match mpls-label
   ```
   ```
   [*AGG-route-policy] apply mpls-label
   ```
   ```
   [*AGG-route-policy] quit
   ```
   ```
   [*AGG] bgp 100
   ```
   ```
   [*AGG-bgp] peer 1.1.1.1 route-policy policy1 export
   ```
   ```
   [*AGG-bgp] peer 3.3.3.3 route-policy policy1 export
   ```
   ```
   [*AGG-bgp] quit
   ```
   ```
   [*AGG] commit
   ```
   
   Repeat this step for the core ABR. For configuration details, see Configuration Files in this section.
6. Verify the configuration.
   
   
   
   After completing the configuration, run the **display ip routing-table** command on a CSG or MASG to view information about a route to the BGP peer's loopback interface.
   
   The following example uses the command output on the CSG.
   
   ```
   <CSG> display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 10       Routes : 10
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
           1.1.1.1/32  Direct  0    0             D  127.0.0.1       LoopBack1
           2.2.2.2/32  OSPF    10   1             D  10.1.1.2        GigabitEthernet0/1/0
           4.4.4.4/32  IBGP    255  0             RD 2.2.2.2         GigabitEthernet0/1/0
          10.1.1.0/24  Direct  0    0             D  10.1.1.1        GigabitEthernet0/1/0
          10.1.1.1/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
        10.1.1.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
         127.0.0.0/8   Direct  0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0 
   ```
   
   Run the **display mpls lsp** command on the CSG or MASG to view LSP information.
   
   The following example uses the command output on the CSG.
   
   ```
   <CSG> display mpls lsp
   ```
   ```
   Flag after Out IF: (I) - RLFA Iterated LSP, (I*) - Normal and RLFA Iterated LSP 
   Flag after LDP FRR: (L) - Logic FRR LSP
   -------------------------------------------------------------------------------
                    LSP Information: LDP LSP
   -------------------------------------------------------------------------------
   FEC                In/Out Label    In/Out IF                      Vrf Name
   1.1.1.1/32         3/NULL          -/-
   2.2.2.2/32         NULL/3          -/GE0/1/0
   2.2.2.2/32         32828/3         -/GE0/1/0
   -------------------------------------------------------------------------------
                    LSP Information: BGP LSP
   -------------------------------------------------------------------------------
   FEC                In/Out Label    In/Out IF                      Vrf Name
   1.1.1.1/32         32829/NULL      -/-
   4.4.4.4/32         NULL/32831      -/-
   ```
   Run the **ping lsp** command on the CSG or MASG to check BGP LSP connectivity. The following example uses the command output on the CSG.
   ```
   <CSG> ping lsp bgp 4.4.4.4 32
   ```
   ```
     LSP PING FEC: BGP LABLED IPV4 PREFIX 4.4.4.4/32/ : 100  data bytes, press CTRL_C to break
       Reply from 4.4.4.4: bytes=100 Sequence=1 time=125 ms
       Reply from 4.4.4.4: bytes=100 Sequence=2 time=3 ms
       Reply from 4.4.4.4: bytes=100 Sequence=3 time=4 ms
       Reply from 4.4.4.4: bytes=100 Sequence=4 time=3 ms
       Reply from 4.4.4.4: bytes=100 Sequence=5 time=3 ms
   
     --- FEC: BGP LABLED IPV4 PREFIX 4.4.4.4/32 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 3/27/125 ms
   ```

#### Configuration Files

* CSG configuration file
  
  ```
  #
  sysname CSG
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   #
   ipv4-family unicast
    network 1.1.1.1 255.255.255.255
    peer 2.2.2.2 enable
    peer 2.2.2.2 route-policy policy1 export
    peer 2.2.2.2 label-route-capability
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  route-policy policy1 permit node 1
   apply mpls-label
  #
  return
  ```
* AGG configuration file
  
  ```
  #
  sysname AGG
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls ldp
  #
  isis 1
   network-entity 10.0000.0000.0000.0010.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
   isis enable 1
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    peer 1.1.1.1 enable
    peer 1.1.1.1 route-policy policy1 export
    peer 1.1.1.1 reflect-client
    peer 1.1.1.1 next-hop-local
    peer 1.1.1.1 label-route-capability
    peer 3.3.3.3 enable
    peer 3.3.3.3 route-policy policy1 export
    peer 3.3.3.3 reflect-client
    peer 3.3.3.3 next-hop-local
    peer 3.3.3.3 label-route-capability
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  route-policy policy1 permit node 1
   if-match mpls-label
   apply mpls-label
  #
  return
  ```
* Core ABR configuration file
  
  ```
  #
  sysname Core ABR
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls ldp
  #
  isis 1
   network-entity 10.0000.0000.0000.0020.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
   isis enable 1
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    peer 2.2.2.2 enable
    peer 2.2.2.2 route-policy policy1 export
    peer 2.2.2.2 reflect-client
    peer 2.2.2.2 next-hop-local
    peer 2.2.2.2 label-route-capability
    peer 4.4.4.4 enable
    peer 4.4.4.4 route-policy policy1 export
    peer 4.4.4.4 reflect-client
    peer 4.4.4.4 next-hop-local
    peer 4.4.4.4 label-route-capability
  #
  ospf 2
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.3.1.0 0.0.0.255
  #
  route-policy policy1 permit node 1
   if-match mpls-label
   apply mpls-label
  #
  return
  ```
* MASG configuration file
  
  ```
  #
  sysname MASG
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.3.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 100
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    network 4.4.4.4 255.255.255.255
    peer 3.3.3.3 enable
    peer 3.3.3.3 route-policy policy1 export
    peer 3.3.3.3 label-route-capability
  #
  ospf 2
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 10.3.1.0 0.0.0.255
  #
  route-policy policy1 permit node 1
   apply mpls-label
  #
  return
  ```